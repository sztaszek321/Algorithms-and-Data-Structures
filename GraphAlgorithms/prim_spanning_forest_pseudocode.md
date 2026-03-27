FUNCTION spanning_forest(start, data)

    CALCULATE sorted list of all edges

    IF start IS empty
        CHOOSE first vertex as start
    END IF

    SET forest TO start vertex
    SET result TO empty list

    WHILE spanning forest is not complete
        FIND smallest edge connecting forest with new vertex

        IF such edge exists
            ADD edge TO result
            ADD new vertex TO forest
            REMOVE chosen edge from edge list
        ELSE
            RAISE error
        END IF
    END WHILE

    RETURN result
END FUNCTION

FUNCTION spanning_forest_main(start, sample)

    VALIDATE sample
    RESULT = CALL spanning_forest(start, sample)
    RETURN result
END FUNCTION