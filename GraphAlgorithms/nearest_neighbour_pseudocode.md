FUNCTION nearest_neighbour(data)

    SET start TO first element of data
    SET edges TO second element of data

    SET path TO start
    SET track TO 0
    SET not_visited TO all nodes except start
    SET node TO start

    WHILE not_visited IS NOT empty
        CALCULATE nearest unvisited neighbour of node

        IF there is no such neighbour
            RAISE error
        END IF

        MOVE to selected neighbour
        UPDATE path
        UPDATE track
        REMOVE selected neighbour from not_visited
    END WHILE

    IF cycle can be closed to start
        ADD start TO path
        UPDATE track
    ELSE
        RAISE error
    END IF

    RETURN path, track
END FUNCTION

FUNCTION nearest_neighbour_main(sample)

    VALIDATE sample
    RESULT = CALL nearest_neighbour(sample)
    RETURN result
END FUNCTION