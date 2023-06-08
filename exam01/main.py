# main.py

import openai

openai.api_key = ''

long_text = """
Translate the following English text to Korea: '지금 우르는 iot시대에 살고 있고, 삶의 편리함과 안전을 제공하고 있다. 나의 생활 패턴을 바꾸어 준다. 다가올 미래가 아닌 현재에 우리는 스마트홈을 누리고 있다.
스마트홈은 다양한 연결된 장치들이 집안의 편의성, 효율성, 보안을 개선하기 위해 상호작용하는 고도로 자동화된 주거 공간을 말합니다. 이런 장치들은 인터넷을 통해 데이터를 공유하고, 집 주변 환경을 모니터링하며, 사용자의 명령에 응답합니다.
스마트홈 기술의 일반적인 예로는 다음과 같은 것들이 있습니다:
스마트 조명: 스마트 조명 시스템은 사용자가 스마트폰 앱 또는 음성 명령을 통해 원격으로 또는 자동화된 스케줄에 따라 조명을 제어할 수 있게 합니다.
스마트 보안: 도어벨 카메라, 보안 카메라, 스마트 도어 락 등의 스마트 보안 장치는 집안의 보안을 강화합니다. 이 장치들은 원격으로 모니터링하고 제어할 수 있으며, 비정상적인 활동이 감지되면 사용자에게 알림을 보냅니다.'
"""

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=f"{long_text}\n\nSummarize:",
  max_tokens=100
)

print(response.choices[0].text.strip())


long_text = """
Translate the following English text to Korea: 'We are living in the age of the Internet of Things (IoT), where smart devices are changing the way we live by making our homes more convenient and safe. Examples of smart home technology include smart lighting, which can be controlled remotely or automatically according to a schedule, and smart security devices like doorbell cameras and security cameras, which can monitor and control activity in the home and send alerts if anything suspicious is detected.'
"""

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=f"{long_text}\n\n:",
  max_tokens=10
)

print(response.choices[0].text.strip())
