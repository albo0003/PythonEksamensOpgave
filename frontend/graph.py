import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def make_graph():
    try:
        
        df = pd.read_csv("/app/data/info.csv")

        
        user = st.session_state["user"]

        df["date"] = pd.to_datetime(df["date"])

        
        df_user = df[df["username"] == user].copy()

        
        df_user = df_user.sort_values("date")

        
        graph = st.selectbox(
            "Vælg data:",
            ["latest", "weight", "height", "bmi"] 
        )

        # latest stats option
        if graph == "latest":

            latest = df_user.iloc[-1]

            st.subheader(f"Seneste data for {user}")

            st.write(f"Dato: {latest['date'].date()}")
            st.write(f"Vægt: {latest['weight']}")
            st.write(f"Højde: {latest['height']}")
            st.write(f"BMI: {round(latest['bmi'], 2)}")
            return f"Dato: {latest['date'].date()} Vægt: {latest['weight']} Højde: {latest['height']} BMI: {round(latest['bmi'], 2)}" 

        else:

            labels = {
                "weight": "Vægt",
                "height": "Højde",
                "bmi": "BMI"
            }

            fig, ax = plt.subplots()

            ax.plot(
                df_user["date"],
                df_user[graph],
                marker="o"
            )

            ax.set_xlabel("Dato")
            ax.set_ylabel(labels[graph])
            ax.set_title(f"{labels[graph]} over tid for {user}")

            plt.xticks(rotation=45)

            st.pyplot(fig)

            # ===== AI STRING DATA =====
            values = np.array(df_user[graph])

            dates = df_user["date"].dt.strftime("%Y-%m-%d").tolist()

            history = []
            for d, v in zip(dates, values):
                history.append(f"{d}: {v}")

            # ===== STATS =====
            avg = np.mean(values)
            low = np.min(values)
            high = np.max(values)

            stats_text = (
                f"Average {graph}: {round(avg, 2)}, "
                f"Lowest {graph}: {low}, "
                f"Highest {graph}: {high}"
            )

            st.info(stats_text)

            return (
                graph + ": " + ", ".join(history) +
                " | " + stats_text +
                (" in centimeters" if graph == "height" else "")
            )

    except Exception as e:
        st.warning("Ingen data endnu")
        st.text(str(e))
        return ""
