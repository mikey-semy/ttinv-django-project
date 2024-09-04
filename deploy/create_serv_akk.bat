@echo off

echo Загрузка переменных окружения...
for /f "tokens=1,2 delims==" %%G in (.env) do (
    set %%G=%%H
)

echo Создание сервисного аккаунта...
yc iam service-account create --name %SERVICE_ACCOUNT_NAME% > service_account_output.txt

echo Получаем ID сервисного аккаунта...
for /f "tokens=2 delims=: " %%a in ('findstr /B "id:" service_account_output.txt') do set "SERVICE_ACCOUNT_ID=%%a"
echo ID сервисного аккаунта получен: %SERVICE_ACCOUNT_ID%

echo Получаем имя или идентификатор каталога, в котором будет размещаться контейнер...
for /f "tokens=2 delims=: " %%a in ('findstr /B "folder_id:" service_account_output.txt') do set "FOLDER_ID=%%a"
echo ID каталога получен: %FOLDER_ID%

echo Удаление временного файла
del service_account_output.txt

echo Обновляем SERVICE_ACCOUNT_ID в .env файле...
(for /f "tokens=1,* delims==" %%a in (.env) do (
    if "%%a"=="SERVICE_ACCOUNT_ID" (
        echo SERVICE_ACCOUNT_ID=%SERVICE_ACCOUNT_ID%
    ) else (
        echo %%a=%%b
    )
)) > .env.tmp
move /y .env.tmp .env
echo Обновляем FOLDER_ID в .env файле...
(for /f "tokens=1,* delims==" %%a in (.env) do (
    if "%%a"=="FOLDER_ID" (
        echo FOLDER_ID=%FOLDER_ID%
    ) else (
        echo %%a=%%b
    )
)) > .env.tmp
move /y .env.tmp .env
echo В .env файле обновлен SERVICE_ACCOUNT_ID=%SERVICE_ACCOUNT_ID% и FOLDER_ID=%FOLDER_ID%

echo Назначение сервисному аккаунту ролей %ROLES%
for %%r in (%ROLES%) do (
    yc resource-manager folder add-access-binding %FOLDER_ID% --role %%r --subject serviceAccount:%SERVICE_ACCOUNT_ID% 
    )