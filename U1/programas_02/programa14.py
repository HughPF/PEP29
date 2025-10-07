# programa14
# Enunciado: Escribe un programa que reciba un número de bytes
# y muestre por pantalla cuántos GBytes, MBytes, KBytes y Bytes son,
# tanto en sistema decimal (SI, 1000) como binario (IEC, 1024).

bytes_input = int(input("Introduce la cantidad de bytes: "))

# Sistema decimal (SI, 1000)
gb_si = bytes_input // (1000**3)
mb_si = (bytes_input % (1000**3)) // (1000**2)
kb_si = (bytes_input % (1000**2)) // 1000
b_si = bytes_input % 1000

# Sistema binario (IEC, 1024)
gib = bytes_input // (1024**3)
mib = (bytes_input % (1024**3)) // (1024**2)
kib = (bytes_input % (1024**2)) // 1024
b_iec = bytes_input % 1024

print(f"{bytes_input} bytes en sistema decimal (SI): {gb_si} GB, {mb_si} MB, {kb_si} KB, {b_si} bytes")
print(f"{bytes_input} bytes en sistema binario (IEC): {gib} GiB, {mib} MiB, {kib} KiB, {b_iec} bytes")
