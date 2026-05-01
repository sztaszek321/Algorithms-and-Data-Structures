FUNCTION hare_niemeyer(data)

    READ M, P, G FROM data

    CALCULATE total number of votes

    SET T TO empty list
    SET R TO empty list

    FOR each party
        CALCULATE quota for this party

        ADD integer part of quota TO T
        ADD decimal remainder of quota TO R
    END FOR

    CALCULATE number of remaining seats

    FOR i FROM 1 TO remaining seats
        FIND party with the highest remainder

        ADD 1 seat TO this party in T
        SET this party remainder TO 0
    END FOR

    RETURN T

END FUNCTION