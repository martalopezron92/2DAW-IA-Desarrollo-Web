# Script para restaurar tildes en el archivo markdown
$file = "bloques\B2_Fundamentos_Tecnicos\U3_Fundamentos_Python_IA.md"

# Leer contenido
$content = Get-Content $file -Raw -Encoding UTF8

# Diccionario de reemplazos comunes
$replacements = @{
    ' por qu ' = ' por qué '
    'Por qu ' = 'Por qué '
    'Qu es' = 'Qué es'
    'Qu son' = 'Qué son'
    'Qu vamos' = 'Qué vamos'
    'especficamente' = 'específicamente'
    'nmeros' = 'números'
    'segn' = 'según'
    'Espaa' = 'España'
    'ms ' = 'más '
    'Razones tcnicas' = 'Razones técnicas'
    'libreras' = 'librerías'
    'bsica' = 'básica'
    'sintaxis bsica' = 'sintaxis básica'
    'Configuracin' = 'Configuración'
    'sesin' = 'sesión'
    'Introduccin' = 'Introducción'
    'Duracin' = 'Duración'
    'milln' = 'millón'
    'sabis' = 'sabéis'
    'prcticos' = 'prácticos'
    'Cul ' = 'Cuál '
    'rpida' = 'rápida'
    'prctico' = 'práctico'
    'Indexacin' = 'Indexación'
    'operacin' = 'operación'
    'operaciones fciles' = 'operaciones fáciles'
    'automtico' = 'automático'
    'automticamente' = 'automáticamente'
    'rea' = 'área'
    'Librera' = 'Librería'
    'anlisis' = 'análisis'
    'fcil' = 'fácil'
    'despus' = 'después'
    'Tambin' = 'También'
    'tambin' = 'también'
    'cdigo' = 'código'
    'versin' = 'versión'
    'FUNDAMENTAL!' = '¡FUNDAMENTAL!'
    'Ojo!' = '¡Ojo!'
    'ser capaz' = 'será capaz'
    'SESIN' = 'SESIÓN'
}

# Aplicar cada reemplazo
foreach ($key in $replacements.Keys) {
    $content = $content -replace [regex]::Escape($key), $replacements[$key]
}

# Guardar archivo
Set-Content $file -Value $content -Encoding UTF8

Write-Host "Tildes restauradas correctamente" -ForegroundColor Green
