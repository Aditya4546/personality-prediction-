document.getElementById('personality-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Stop the default form submission

    const form = event.target;
    
    // 1. Collect the 7 input values
    const data = {
        gender: form.gender.value,
        age: parseInt(form.age.value), // Convert to number
        openness: parseInt(form.openness.value),
        neuroticism: parseInt(form.neuroticism.value),
        conscientiousness: parseInt(form.conscientiousness.value),
        agreeableness: parseInt(form.agreeableness.value),
        extraversion: parseInt(form.extraversion.value)
    };

    try {
        // 2. Send the data to the Python Flask server
        const response = await fetch('http://127.0.0.1:5000/predict_personality', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data) // Send data as a JSON string
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // 3. Get the JSON response from the server
        const result = await response.json();

        // 4. Update the website with the results
        // document.getElementById('person-no-output').textContent = `Person No: ${result.person_no}`;
        document.getElementById('personality-output').textContent = `Predicted Personality: ${result.predicted_personality}`;

    } catch (error) {
        console.error('Error:', error);
        document.getElementById('personality-output').textContent = 'An error occurred during prediction.';
    }
});