import re

# Leer el archivo
with open(r'bloques\B2_Fundamentos_Tecnicos\U3_Fundamentos_Python_IA.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Patrón para eliminar emojis pero mantener caracteres españoles
# Este patrón elimina la mayoría de emojis manteniendo letras acentuadas y ñ
emoji_pattern = re.compile("["
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    u"\U00002702-\U000027B0"
    u"\U000024C2-\U0001F251"
    u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    u"\U00002600-\U000026FF"  # Miscellaneous Symbols
    u"\U0001FA00-\U0001FAFF"  # Chess Symbols
    "]+", flags=re.UNICODE)

# Eliminar emojis
content_sin_emojis = emoji_pattern.sub('', content)

# También eliminar espacios dobles que puedan quedar
content_sin_emojis = re.sub(r' +', ' ', content_sin_emojis)

# Guardar el archivo limpio
with open(r'bloques\B2_Fundamentos_Tecnicos\U3_Fundamentos_Python_IA.md', 'w', encoding='utf-8') as f:
    f.write(content_sin_emojis)

print("✓ Emojis eliminados correctamente")
print(f"Tamaño original: {len(content)} caracteres")
print(f"Tamaño final: {len(content_sin_emojis)} caracteres")
print(f"Caracteres eliminados: {len(content) - len(content_sin_emojis)}")
