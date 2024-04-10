document.addEventListener('DOMContentLoaded', (event) => {
    // Get all checkboxes
    const checkboxes = document.querySelectorAll('.form-check-input');

    // Get the list where we'll display the loadout choices
    const loadoutList = document.querySelector('.list-group');

    // Add an event listener to each checkbox
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', (event) => {
            // If the checkbox is checked, add the loadout choice to the list
            if (event.target.checked) {
                const listItem = document.createElement('li');
                listItem.textContent = event.target.value;
                listItem.classList.add('list-group-item');
                loadoutList.appendChild(listItem);
            } 
            // If the checkbox is unchecked, remove the loadout choice from the list
            else {
                const listItems = loadoutList.querySelectorAll('.list-group-item');
                listItems.forEach(item => {
                    if (item.textContent === event.target.value) {
                        loadoutList.removeChild(item);
                    }
                });
            }

            // If there are 4 loadout choices selected, disable all checkboxes
            if (loadoutList.querySelectorAll('.list-group-item').length >= 4) {
                checkboxes.forEach(checkbox => {
                    checkbox.disabled = true;
                });
            } 
            // If there are less than 4 loadout choices selected, enable all checkboxes
            else {
                checkboxes.forEach(checkbox => {
                    checkbox.disabled = false;
                });
            }
        });
    });
});