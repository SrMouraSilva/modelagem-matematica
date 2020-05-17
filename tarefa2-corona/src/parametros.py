from dataclasses import dataclass


@dataclass
class Parametros:
    pais: str

    N_UTI: float
    C_UTI: float

    μ: float
    υ: float
    σ: float

    β: float
    γ: float
    ρ: float

    P_0: float
    Y_0: float = 1

    tempo_step: int = 1
    numero_dias: float = 365.0