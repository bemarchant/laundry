document.addEventListener("DOMContentLoaded", function () {
  var machineSelect = document.getElementById("machine");
  var slotSelect = document.getElementById("slot");

  function populateSlotSelect() {
    var selectedMachine = machineSelect.value;
    slotSelect.innerHTML = "";

    var url = `/laundry/booking/get_available_slots/${selectedMachine}/`;

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        var slotOptions = data.slot_available;
        for (var i = 0; i < slotOptions.length; i++) {
          var option = document.createElement("option");
          option.value = slotOptions[i];
          option.text = slotOptions[i];
          slotSelect.appendChild(option);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
  print("### script.js");
  const now = new Date();
  const currentHour = now.getHours();
  const currentMinute = now.getMinutes();

  const roundedMinutes = Math.ceil(currentMinute / 15) * 15;

  const availableHours = [];
  for (let hour = currentHour; hour <= 23; hour++) {
    for (let minute = 0; minute < 60; minute += 15) {
      if (
        hour > currentHour ||
        (hour === currentHour && minute >= roundedMinutes)
      ) {
        availableHours.push(`${hour}:${minute.toString().padStart(2, "0")}`);
      }
    }
  }
  const startTimeSelect = document.getElementById("start_time");

  availableHours.forEach((hour) => {
    const option = document.createElement("option");
    option.value = hour;
    option.textContent = hour;
    startTimeSelect.appendChild(option);
  });

  machineSelect.addEventListener("change", populateSlotSelect);
});
