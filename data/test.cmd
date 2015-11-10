@set old_dir=%1
@set new_dir=%old_dir:\=/%
@echo %old_dir%
@echo %new_dir%
@set ls_cmd=ls -d %new_dir%/*/
SETLOCAL ENABLEDELAYEDEXPANSION
FOR /f %%G IN ('%ls_cmd%') DO (
	@echo %%G
	@test.cmd %%G
)
 

@Pause
