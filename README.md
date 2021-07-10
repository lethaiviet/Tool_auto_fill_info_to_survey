[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/lethaiviet/Tool_auto_fill_info_to_survey">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Auto fill the info to the survey</h3>

  <p align="center">
    The tool uses selenium
    <br />
    <a href="https://github.com/lethaiviet/Tool_auto_fill_info_to_survey">View Demo</a>
    ·
    <a href="https://github.com/lethaiviet/Tool_auto_fill_info_to_survey">Report Bug</a>
    ·
    <a href="https://github.com/lethaiviet/Tool_auto_fill_info_to_survey">Request Feature</a>
  </p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Input: 
```json
//config.json
{
    "URL_VIEW_FORM": "https://docs.google.com/forms/d/e/1FAIpQLSdBqQ_YJIP7zM4enptfJFkqdgVn-wqBUBGRLHvLHkLJbFWENw/viewform",
    "LOCATOR": {
        "TEXT_BOX": "//div[contains(@data-params, '%s')]/div/div[2]/div/div/div/div/input",
        "RADIO_BUTTON": "//div[contains(@data-params, '%s')]/div/div[2]/div/div/span/div/div/label/div/div/div[@data-value='%s']"
    },
    "ACTIONS": [
        {
            "DESCRIPTION": "1. Họ tên nhân viên",
            "TYPE": "TEXT_BOX",
            "INPUT_DATA": "Nguyễn Văn A"
        },
        {
            "DESCRIPTION": "2. Mã số nhân viên",
            "TYPE": "TEXT_BOX",
            "INPUT_DATA": "123456"
        },
        {
            "DESCRIPTION": "3. Điện thoại liên hệ",
            "TYPE": "TEXT_BOX",
            "INPUT_DATA": "123456789"
        },
        {
            "DESCRIPTION": "5. Trong 24 giờ (hoặc 48 giờ nếu ngày khai báo là thứ Hai hàng tuần) qua bạn có tiếp xúc F0/1/2/3 hoặc người nào đó có nguy cơ nhiễm Covid-19 không (tại địa phương hoặc từ nơi khác đến/về)?",
            "TYPE": "RADIO_BUTTON",
            "INPUT_DATA": "Không"
        },
        {
            "DESCRIPTION": "7. Trong 24 giờ qua bạn có đến những nơi có nguy cơ cao về Covid-19 không (theo thông báo của CDC)?",
            "TYPE": "RADIO_BUTTON",
            "INPUT_DATA": "Không"
        },
        {
            "DESCRIPTION": "9. Nơi bạn ở nằm ngoài, trong, hay bên cạnh khu vực đang tạm phong tỏa?",
            "TYPE": "RADIO_BUTTON",
            "INPUT_DATA": "Ngoài"
        },
        {
            "DESCRIPTION": "10. Ngay lúc này, bạn tự đánh giá bản thân thuộc diện an toàn đối với nguy cơ bị lây nhiễm Covid nào theo 3 mức sau:",
            "TYPE": "RADIO_BUTTON",
            "INPUT_DATA": "Tuyệt đối an toàn"
        },
        {
            "DESCRIPTION": "12. Ngày tháng năm thực hiện khai báo",
            "TYPE": "TEXT_BOX",
            "INPUT_DATA": "today"
        }
    ]
}
```

Output:
All fields will be filled automatically as the image below:

[![File excel][file-excel]](https://github.com/lethaiviet/ToolConverterExcelToJson/blob/main/images/image01.PNG)

### Built With

* [selenium](https://selenium-python.readthedocs.io/) - Selenium is an open-source tool that automates web browsers

### Prerequisites

* [Python3](https://www.python.org/downloads/)
* [Python Virtual Environments](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
  

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/lethaiviet/Tool_auto_fill_info_to_survey.git
   ```
2. Create virtual environment
   ```sh
    cd Tool_auto_fill_info_to_survey
    00_install_env.bat
   ```
3. Active virtual environment
   ```sh
    01_active_env.bat
   ```
4. Install dependency libraries on the virtual environment
   ```sh
    02_install_libs.bat
   ```

NOTE: if you want to create Executable from Python Script
   ```sh
    03_create_app.bat
   ```
  After running successfully, the exe output in the path `Tool_auto_fill_info_to_survey\dist\ToolFillInfoSurvey.exe`
<!-- USAGE EXAMPLES -->
## Usage
1. Go to the folder `Tool_auto_fill_info_to_survey\dist\`
2. Modify your info in `config.json`
3. Double click to `ToolFillInfoSurvey.exe`
4. Make sure all info fill to survey is correct
5. Click "Submit" button on the survey

<!-- CONTACT -->
## Contact
Project Link: [https://github.com/lethaiviet/Tool_auto_fill_info_to_survey](https://github.com/lethaiviet/Tool_auto_fill_info_to_survey)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/lethaiviet/Tool_auto_fill_info_to_survey.svg?style=for-the-badge
[contributors-url]: https://github.com/lethaiviet/Tool_auto_fill_info_to_survey/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/lethaiviet/Tool_auto_fill_info_to_survey.svg?style=for-the-badge
[forks-url]: https://github.com/lethaiviet/Tool_auto_fill_info_to_survey/graphs/network/members
[stars-shield]: https://img.shields.io/github/stars/lethaiviet/Tool_auto_fill_info_to_survey.svg?style=for-the-badge
[stars-url]: https://github.com/lethaiviet/Tool_auto_fill_info_to_survey/graphs/stargazers
[issues-shield]: https://img.shields.io/github/issues/lethaiviet/Tool_auto_fill_info_to_survey.svg?style=for-the-badge
[issues-url]: https://github.com/lethaiviet/Tool_auto_fill_info_to_survey/graphs/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]:https://github.com/lethaiviet/Tool_auto_fill_info_to_survey/graphs/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[file-excel]: images/image01.PNG
