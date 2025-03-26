import requests


class RecaptchaService:
    @staticmethod
    # проверка под рекапчу
    def get_recaptcha_token(driver):
        try:
            token = driver.execute_script("""
                return new Promise((resolve) => {
                    grecaptcha.ready(function() {
                        grecaptcha.execute('6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI', {action: 'submit'})
                            .then(function(token) {
                                resolve(token);
                            });
                    });
                });
            """)
            return token
        except Exception as e:
            print(f"Error getting reCAPTCHA token: {e}")
            return None

    @staticmethod
    def verify_recaptcha(recaptcha_response):
        secret_key = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
        payload = {
            'secret': secret_key,
            'response': recaptcha_response
        }

        try:
            response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
            response.raise_for_status()
            result = response.json()
            print(f"reCAPTCHA verification result: {result}")
            return result.get('success', False)
        except requests.exceptions.RequestException as e:
            print(f"reCAPTCHA verification error: {e}")
            return False