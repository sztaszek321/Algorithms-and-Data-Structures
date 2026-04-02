FUNCTION smallest_last(data)

    CALCULATE vertex dictionary with degrees and neighbors
    SET cp TO copy of vertex dictionary
    SET deletes TO empty list
    SET colors TO empty dictionary

    WHILE cp is not empty
        CHOOSE first vertex from cp
        INSERT chosen vertex at beginning of deletes
        REMOVE chosen vertex from cp
        DELETE chosen vertex from neighbor lists in cp
        DECREASE degrees of adjacent vertices
        SORT cp by degree in ascending order
    END WHILE

    FOR each vertex v in deletes
        SET flag TO false

        FOR each color c in colors
            IF all vertices in color c are non-neighbors of v
                ADD v TO color c
                SET flag TO true
                BREAK
            END IF
        END FOR

        IF flag IS false
            CREATE new color containing v
        END IF
    END FOR

    RETURN colors

END FUNCTION


FUNCTION smallest_last_main(sample)

    VALIDATE sample
    RESULT = CALL smallest_last(sample)
    RETURN result

END FUNCTION