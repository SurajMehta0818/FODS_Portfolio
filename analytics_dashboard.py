import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data_loader import load_grades, load_eca_data


class AnalyticsDashboard(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Analytics Dashboard")
        self.geometry("900x700")

        tk.Label(self, text="Analytics Dashboard", font=("Arial", 16)).pack(pady=10)

        # Tabs
        tab_control = ttk.Notebook(self)
        self.grade_tab = ttk.Frame(tab_control)
        self.eca_tab = ttk.Frame(tab_control)
        tab_control.add(self.grade_tab, text="Grades Overview")
        tab_control.add(self.eca_tab, text="ECA Participation")
        tab_control.pack(expand=1, fill='both')

        self.show_grade_analysis()
        self.show_eca_analysis()

    def show_grade_analysis(self):
        grades_data = load_grades()
        if not grades_data:
            tk.Label(self.grade_tab, text="No grades data available").pack()
            return

        subject_count = max(len(grades) for grades in grades_data.values())
        avg_grades = [0] * subject_count
        total_students = len(grades_data)

        for grades in grades_data.values():
            for i, mark in enumerate(grades):
                avg_grades[i] += int(mark)

        avg_grades = [round(score / total_students, 2) for score in avg_grades]
        subjects = [f"Subject {i+1}" for i in range(subject_count)]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(subjects, avg_grades, color='green')
        ax.set_title("Average Grades per Subject")
        ax.set_ylabel("Average Marks")
        ax.set_ylim(0, 100)

        canvas = FigureCanvasTkAgg(fig, master=self.grade_tab)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Top Performing Students
        student_totals = {student: sum(grades) for student, grades in grades_data.items()}
        sorted_students = sorted(student_totals.items(), key=lambda x: x[1], reverse=True)

        top_frame = tk.Frame(self.grade_tab)
        top_frame.pack(pady=10)
        tk.Label(top_frame, text="Top Performing Students:", font=('Arial', 12, 'bold')).pack(anchor='w')

        for student, total in sorted_students[:3]:  # Show top 3
            tk.Label(top_frame, text=f"{student} - Total Marks: {total}").pack(anchor='w')

    def show_eca_analysis(self):
        eca_data = load_eca_data()
        if not eca_data:
            tk.Label(self.eca_tab, text="No ECA data available").pack()
            return

        activity_count = {}
        for activities in eca_data.values():
            for activity in activities:
                activity_count[activity] = activity_count.get(activity, 0) + 1

        activities = list(activity_count.keys())
        counts = list(activity_count.values())

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.pie(counts, labels=activities, autopct='%1.1f%%', startangle=90)
        ax.set_title("ECA Participation Distribution")

        canvas = FigureCanvasTkAgg(fig, master=self.eca_tab)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Most Active Students
        student_activity_count = {student: len(activities) for student, activities in eca_data.items()}
        sorted_activity = sorted(student_activity_count.items(), key=lambda x: x[1], reverse=True)

        active_frame = tk.Frame(self.eca_tab)
        active_frame.pack(pady=10)
        tk.Label(active_frame, text="Most Active Students in ECAs:", font=('Arial', 12, 'bold')).pack(anchor='w')

        for student, count in sorted_activity[:3]:  # Top 3
            tk.Label(active_frame, text=f"{student} - {count} activities").pack(anchor='w')

        # Most Popular Activities
        popular_activities = sorted(activity_count.items(), key=lambda x: x[1], reverse=True)
        tk.Label(active_frame, text="\nTop 3 Most Popular Activities:", font=('Arial', 12, 'bold')).pack(anchor='w')
        for activity, count in popular_activities[:3]:
            tk.Label(active_frame, text=f"{activity}: {count} participants").pack(anchor='w')
