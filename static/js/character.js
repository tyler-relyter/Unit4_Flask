document.addEventListener('DOMContentLoaded', (event) => {
    // Get all radio buttons
    const radios = document.querySelectorAll('.form-check-input');

    // Get the character div where we'll display the selected options
    const characterDiv = document.querySelector('#character');

    // Create an object to store the selected options
    const selectedOptions = {};

    // Add an event listener to each radio button
    radios.forEach(radio => {
        radio.addEventListener('change', (event) => {
            // If the radio button is selected, add the option to the selectedOptions object
            if (event.target.checked) {
                const optionType = event.target.name;
                const optionValue = event.target.value;
                selectedOptions[optionType] = optionValue;
            }

            // Clear the character div
            characterDiv.innerHTML = '';

            // Add the selected options to the character div
            for (const optionType in selectedOptions) {
                const optionValue = selectedOptions[optionType];
                const optionElement = document.createElement('p');
                optionElement.textContent = `${optionType}: ${optionValue}`;
                characterDiv.appendChild(optionElement);
            }
        });
    });
});