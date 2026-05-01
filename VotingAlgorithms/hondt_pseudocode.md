FUNCTION hondt(data)

    READ M, P, G FROM data

    SET T TO array of P zeros
    SET F TO copy of G

    FOR i FROM 1 TO M
        FIND index of party with the highest value in F

        ADD 1 seat TO this party in T

        CALCULATE new vote factor for this party:
            F[index] = G[index] / (T[index] + 1)
    END FOR

    RETURN T

END FUNCTION