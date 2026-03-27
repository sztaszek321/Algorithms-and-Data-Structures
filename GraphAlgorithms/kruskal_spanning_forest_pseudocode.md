FUNCTION kruskal(data)

    CALCULATE list of all edges
    SORT edges by weight

    SET forest TO separate sets of vertices
    SET result TO empty list

    WHILE there are edges AND spanning forest is not complete
        TAKE edge with smallest weight

        IF its vertices are in different sets
            ADD edge TO result
            MERGE sets of its vertices
        END IF
    END WHILE

    RETURN result
END FUNCTION

FUNCTION kruskal_main(sample)

    VALIDATE sample
    RESULT = CALL kruskal(sample)
    RETURN result
END FUNCTION