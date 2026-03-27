FUNCTION johnson(data)

    SET edges TO data

    CALCULATE graph with new apex q
    CALCULATE Bellman-Ford from q
    CALCULATE new edge weights

    SET result TO empty list

    FOR EACH apex IN edges
        CALCULATE Dijkstra from apex
        CALCULATE correct final weights
        ADD result for apex TO result
    END FOR

    RETURN result
END FUNCTION

FUNCTION johnson_main(sample)

    VALIDATE sample
    RESULT = CALL johnson(sample)
    RETURN result
END FUNCTION