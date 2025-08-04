import streamlit as     submitted = st.form_submit_button("Add Student")

    if submitted and name:
        total = mark1 + mark2 + mark3
        average = total / 3
        grade = calculate_grade(average)
        st.session_state.students.append({
            'name': name,
            'marks': [mark1, mark2, mark3],
            'total': total,
            'average': average,
            'grade': grade
        })
        st.success(f"{name}'s data added successfully!")

# Show student summary
if st.session_state.students:
    st.subheader("📋 Student Summary")
    for student in st.session_state.students:
        st.write(f"**{student['name']}**")
        st.write(f"Marks: {student['marks']}")
        st.write(f"Total: {student['total']}")
        st.write(f"Average: {student['average']:.2f}")
        st.write(f"Grade: {student['grade']}")
        st.markdown("---")

    # Class average
    class_avg = sum(s['average'] for s in st.session_state.students) / len(st.session_state.students)
    st.subheader(f"📊 Class Average: {class_avg:.2f}")

    # Topper
    topper = max(st.session_state.students, key=lambda s: s['total'])
    st.subheader(f"🏆 Topper: {topper['name']} with {topper['total']} marks")

# Clear all data
if st.button("🗑️ Clear All Data"):
    st.session_state.students = []
    st.success("All student data cleared!")
st

# Grade calculator
def calculate_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

# App title
st.title("🎓 Student Marks & Grade Summary")

# Session state to store student data
if 'students' not in st.session_state:
    st.session_state.students = []

# Input form
with st.form("student_form"):
    name = st.text_input("Student Name")
    mark1 = st.number_input("Subject 1 Marks", min_value=0.0, max_value=100.0)
    mark2 = st.number_input("Subject 2 Marks", min_value=0.0, max_value=100.0)
    mark3 = st.number_input("Subject 3 Marks", min_value=0.0, max_value=100.0)
