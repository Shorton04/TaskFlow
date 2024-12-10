// Handle dragging
document.querySelectorAll(".task").forEach((task) => {
  task.addEventListener("dragstart", (e) => {
    task.classList.add("is-dragging");
  });

  task.addEventListener("dragend", (e) => {
    task.classList.remove("is-dragging");
  });
});

// Handle dragover and drop
document.querySelectorAll(".swim-lane").forEach((lane) => {
  lane.addEventListener("dragover", (e) => {
    e.preventDefault();
    const task = document.querySelector(".is-dragging");
    if (task) {
      lane.appendChild(task);
    }
  });

  lane.addEventListener("drop", (e) => {
    e.preventDefault();
    const task = document.querySelector(".is-dragging");
    if (!task) return;
    task.classList.remove("is-dragging");

    // Get task ID and new status
    const taskId = task.dataset.id;
    const newStatus =
      lane.id === "todo-lane"
        ? "pending"
        : lane.id === "done-lane"
        ? "completed"
        : "in_progress";

    // Update task status in the backend
    fetch(`/update-task-status/${taskId}/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
          .value,
      },
      body: JSON.stringify({ status: newStatus }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to update task status");
        }
        return response.json();
      })
      .then((data) => {
        if (data.status !== "success") {
          alert("Error updating task: " + data.message);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const projectSelect = document.getElementById("project-select");
  const tasks = document.querySelectorAll(".task");

  // Event listener for when the project is changed
  projectSelect.addEventListener("change", function () {
    const selectedProjectId = projectSelect.value;

    tasks.forEach((task) => {
      const taskProjectId = task.getAttribute("data-project-id");

      // If the task's project matches the selected one (or if 'All Projects' is selected)
      if (selectedProjectId === "" || taskProjectId === selectedProjectId) {
        task.style.display = ""; // Show the task
      } else {
        task.style.display = "none"; // Hide the task
      }
    });
  });

  // Trigger the change event on page load to apply the initial filter
  projectSelect.dispatchEvent(new Event("change"));
});
