document.addEventListener("DOMContentLoaded", function () {
  var machineSelect = document.getElementById("machine");
  var slotOptions = document.getElementById("slotOptions");
  var hourOption = document.getElementById("hourSelect");
  var quarterOption = document.getElementById("quarterSelect");
  var dayBlock = document.getElementById("dayBlockLabel");

  function populateMachineAvailability() {
    var selectedMachineOption =
      machineSelect.options[machineSelect.selectedIndex];
    var machineId = selectedMachineOption.getAttribute("data-machine-id");
    var url = `/laundry/get_machine_availability/${machineId}/`;

    fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        hourOption.innerHTML = "";
        for (let hour = 0; hour <= 24; hour++) {
          const option = document.createElement("option");
          const hourString = hour.toString().padStart(2, "0"); // Format as "00", "01", etc.
          option.value = hourString;
          option.text = hourString;
          hourOption.appendChild(option);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  function fillDayBlock() {
    const selectedHour = parseInt(hourOption.value, 10);
    if (selectedHour < 12) {
      dayBlock.textContent = "AM";
    } else {
      dayBlock.textContent = "PM";
    }
  }
  machineSelect.addEventListener("change", populateMachineAvailability);
  hourOption.addEventListener("change", fillDayBlock);
});
