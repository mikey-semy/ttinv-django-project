@echo off

echo Loading environment variables...
for /f "tokens=1,2 delims==" %%G in (.env) do (
    set %%G=%%H
)

echo Creating container...
docker build --platform=linux/amd64 --pull --rm -f "../Dockerfile" -t %DOCKER_NAME%:latest ".."
echo Container created successfully.

echo Creating new container registry...
yc container registry create --name %DOCKER_NAME% > registry_output.txt
echo Container registry created.

echo Extracting registry ID...
for /f "tokens=2 delims=: " %%a in ('findstr /B "id:" registry_output.txt') do set "REGISTRE_ID=%%a"
echo Registry ID extracted: %REGISTRE_ID%

echo Removing temporary file...
del registry_output.txt

echo Updating .env file...
(for /f "tokens=1,* delims==" %%a in (.env) do (
    if "%%a"=="REGISTRE_ID" (
        echo REGISTRE_ID=%REGISTRE_ID%
    ) else (
        echo %%a=%%b
    )
)) > .env.tmp
move /y .env.tmp .env
echo .env file updated.

echo Authenticating with Yandex Cloud...
yc container registry configure-docker
echo Authentication complete.

echo Creating Docker tag...
docker tag %DOCKER_NAME% cr.yandex/%REGISTRE_ID%/%DOCKER_NAME%:latest
echo Docker tag created.

echo Pushing container to Yandex Cloud...
docker push cr.yandex/%REGISTRE_ID%/%DOCKER_NAME%:latest
echo Container pushed successfully.

::echo Creating serverless container...
::yc serverless container create --name %DOCKER_NAME%
::echo Serverless container created.

echo Deploying image to container...
yc serverless container revision deploy ^
  --container-name %DOCKER_NAME% ^
  --image "cr.yandex/%REGISTRE_ID%/%DOCKER_NAME%:latest" ^
  --cores %CORES% ^
  --memory %MEMORY% ^
  --concurrency %CONCURRENCY% ^
  --execution-timeout %EXECUTION_TIMEOUT% ^
  --service-account-id %SERVICE_ACCOUNT_ID% ^
  --environment DB_DIALECT="%DB_DIALECT%" ^
  --environment DB_DRIVERNAME="%DB_DRIVERNAME%" ^
  --environment DB_NAME="%DB_NAME%" ^
  --environment DB_HOST="%DB_HOST%" ^
  --environment DB_USERNAME="%DB_USERNAME%" ^
  --environment DB_PASSWORD="%DB_PASSWORD%" ^
  --environment DB_PORT="%DB_PORT%"
echo Deployment complete.

echo Installation process finished successfully.
