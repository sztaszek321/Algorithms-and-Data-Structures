FUNCTION sainte_lague(data)

    SET M TO number of seats from data
    SET P TO number of parties from data
    SET G TO array of votes from data

    SET T TO array of P zeros
    SET F TO copy of G

    FOR i FROM 1 TO M
        FIND index of party with the highest value in F

        ADD 1 seat TO this party in T

        CALCULATE new vote factor for this party:
            F[index] = G[index] / (2 * T[index] + 1)
    END FOR

    RETURN T

END FUNCTION