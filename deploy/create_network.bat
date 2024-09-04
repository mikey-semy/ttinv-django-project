@echo off

echo Loading environment variables...
for /f "tokens=1,2 delims==" %%G in (.env) do (
    set %%G=%%H
)

yc vpc network create --name %NETWORK_NAME%

