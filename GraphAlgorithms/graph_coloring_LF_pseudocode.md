FUNCTION largest_first(data)

    CALCULATE degrees and neighbors for all vertices
    SORT vertices by degree in descending order
    SET colors TO empty dictionary

    FOR each vertex in sorted vertices
        SET assigned TO false

        FOR each color class in colors
            IF vertex is not adjacent to any vertex in this color class
                ADD vertex TO this color class
                SET assigned TO true
                BREAK
            END IF
        END FOR

        IF assigned IS false
            CREATE new color class containing this vertex
        END IF
    END FOR

    RETURN colors

END FUNCTION


FUNCTION largest_first_main(sample)

    VALIDATE sample
    RESULT = CALL largest_first(sample)
    RETURN result

END FUNCTION