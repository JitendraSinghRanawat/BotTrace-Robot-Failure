import pandas as pd


def detect_failures(df):
    """
    Detect possible robot failure conditions from robot log data.

    Parameters:
        df: DataFrame containing robot sensor and motor data.

    Returns:
        DataFrame with a new column named 'detected_error'.
    """

    detected_errors = []

    for index, row in df.iterrows():
        # By default, assume the robot is working normally
        error = "NORMAL"

        # Check if the battery voltage is low
        if row["battery"] < 6.9:
            error = "LOW_BATTERY"

        # Check if the robot stopped because an obstacle is too close
        if row["distance"] < 10 and row["left_motor"] == 0 and row["right_motor"] == 0:
            error = "OBSTACLE_STOP"

        # Check if left and right motor speeds are very different
        if abs(row["left_motor"] - row["right_motor"]) > 80:
            error = "MOTOR_IMBALANCE"

        # Check if the robot is tilted too much
        if row["tilt"] > 20:
            error = "ROBOT_TILT_WARNING"

        # Store the detected error for this row
        detected_errors.append(error)

    # Add all detected errors as a new column in the data
    df["detected_error"] = detected_errors

    return df


if __name__ == "__main__":
    # Read robot log data from CSV file
    robot_data = pd.read_csv("data/sample_robot_log.csv")

    # Analyze the robot data and detect failures
    analyzed_data = detect_failures(robot_data)

    # Save the analyzed data into a new CSV file
    analyzed_data.to_csv("data/analyzed_robot_log.csv", index=False)

    print("Analysis completed. File saved in data/analyzed_robot_log.csv")