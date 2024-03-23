<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Send Email</title>
    <style>
        body {
            background-color: #1a1a1a;
            color: #fff;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        form {
            background-color: #292929;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            width: 300px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        textarea {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
            background-color: #1a1a1a;
            color: #fff;
            resize: none;
        }

        input[type="submit"] {
            background-color: #00ffcc;
            color: #1a1a1a;
            border: none;
            padding: 10px 20px;
            margin-top: 10px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        input[type="submit"]:hover {
            background-color: #009688;
        }

        select {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
            background-color: #1a1a1a;
            color: #fff;
        }
    </style>
</head>

<body>

    <form id="emailForm">
        <label for="body" style="color: #00ffcc;">Body:</label><br>
        <textarea id="body" name="body" rows="5" cols="30" placeholder="Enter your message here..." required>
Hello Tutor! This is an automated email from BridgeTheGap asking for you to tutor me. Please reply to this email if you can tutor me. My preferred language is [Preferred Language], so please Google translate your future email in that language. Thank you!
    </textarea>
        <br>
        <label for="languageSelect" style="color: #00ffcc;">Preferred Language:</label>
        <select id="languageSelect">
            <option value="english">English</option>
            <option value="spanish">Español</option>
            <option value="french">Français</option>
            <option value="dutch">Deutsch</option>
            <option value="italian">Italiano</option>
            <option value="hindi">हिन्दी</option>
            <!-- Add more language options as needed -->
        </select>
        <br>
        <input type="submit" value="Send Email">
    </form>

    <script>
        document.getElementById("emailForm").addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent the form from submitting normally

            // Retrieve form data
            const body = document.getElementById("body").value;
            const preferredLanguage = document.getElementById("languageSelect").value;

            // Constants
            const toEmail = "tutorsemail@email.com";
            const subject = "Automated Tutor Request from BridgeTheGap";

            // Insert preferred language into the email body
                   const emailBody = body.replace("[Preferred Language]", "[" + preferredLanguage + "]");


            // Construct mailto URL
            const mailtoURL = `mailto:${toEmail}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(emailBody)}`;

            // Open email client in new tab
            window.open(mailtoURL, "_blank");
        });
    </script>

</body>

</html>
