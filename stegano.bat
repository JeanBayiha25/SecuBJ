@echo off

setlocal

set image="chemin/vers/image.png"
set output_image="chemin/vers/image_cachee.png"
set text="Texte à cacher"

rem Convertir le texte en binaire
for /f "usebackq delims=" %%a in ('echo %text% ^| xxd -b -c 1 ^| findstr /r /c:"[01] [01] "') do (
    set "binary_text=!binary_text!%%a"
)

rem Cacher le texte dans l'image en modifiant les bits de poids faible
magick %image% -depth 8 -colorspace RGB ^
    -size %binary_text:~0,-1% ^
    -define png:bit-depth=1 ^
    -compress none ^
    -channel R -fx "i&1 ? (u&254)+1 : u&254" ^
    -channel G -fx "i&1 ? (v&254)+1 : v&254" ^
    -channel B -fx "i&1 ? (w&254)+1 : w&254" ^
    %output_image%

echo Texte caché dans l'image avec succès.

endlocal
