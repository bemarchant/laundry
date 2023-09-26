document.addEventListener("DOMContentLoaded", function () {
  var machineSelect = document.getElementById("machine");
  var slotSelect = document.getElementById("slot");

  function populateSlotSelect() {
    var selectedMachine = machineSelect.value;
    slotSelect.innerHTML = "";

    var url = `/app/booking/get_available_slots/${selectedMachine}/`;

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        var slotOptions = data.slot_available;

        for (var i = 0; i < slotOptions.length; i++) {
          var option = document.createElement("option");
          option.text = slotOptions[i];
          slotSelect.appendChild(option);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  machineSelect.addEventListener("change", populateSlotSelect);
  populateSlotSelect();
});
