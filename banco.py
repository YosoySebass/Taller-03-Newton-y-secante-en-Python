def secante(f, p0, p1, TOL=1e-6, N0=50):
    """Algoritmo 2.4. Devuelve (p, historia), con historia = [p0, p1, p2, ..., p]."""
    # Paso 1: i = 2; q0 = f(p0); q1 = f(p1); historia empieza con p0 y p1.
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    historia = [p0, p1]

    # Paso 2: mientras i <= N0, haga los pasos 3 a 6.
    while i <= N0:
        # Si q1 == q0, la secante es horizontal: lance un ZeroDivisionError con un mensaje claro.
        if q1 == q0:
            raise ZeroDivisionError(f"q1 == q0 en p1={p1} y p0={p0}: la secante es horizontal (división por cero).")

        # Paso 3: calcule p y agréguelo a la historia. (Nota el operador * de multiplicación)
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        historia.append(p)

        # Paso 4: si |p - p1| < TOL, devuelva (p, historia).
        if abs(p - p1) < TOL:
            return p, historia

        # Paso 5: i = i + 1.
        i = i + 1

        # Paso 6: corra los puntos (p0, q0) <- (p1, q1) y (p1, q1) <- (p, f(p)).
        p0, q0 = p1, q1
        p1, q1 = p, f(p)

    # Paso 7: lance un RuntimeError si se agotan las iteraciones
    raise RuntimeError(f"El metodo fracaso despues de {N0} iteraciones")


def saldo_final(i, monto=20000.0, cuota=450.0, meses=60):
    """Saldo después de pagar todas las cuotas, con interés mensual i (0.01 es 1 %)."""
    saldo = monto
    for mes in range(meses):
        saldo = saldo * (1 + i) - cuota       # COMPLETE: interés del mes y pago de la cuota
    return saldo


mensual, historia = secante(saldo_final, 0.005, 0.02, TOL=1e-10)

print(mensual)
# print(historia)

tasaEfectivaAnual = (1 + mensual)**12 - 1
print(tasaEfectivaAnual)

print(saldo_final(0))
print(f"Porcentaje del interes mensual es: {mensual*100:.4f}")
print(f"Porcentaje de la tasa efectiva anual con dos decimales es: {tasaEfectivaAnual*100:.2f}")