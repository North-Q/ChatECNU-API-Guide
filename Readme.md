#  ChatECNU 大模型 API 使用指南



> - **作者**：qmh_se@qq.com
> - **版本**：v1.0
> - **更新日期**：2025年3月10日
> - **说明**：
>   - 本文档主要基于[华东师范大学开发者平台](https://developer.ecnu.edu.cn/vitepress/llm/model.html) 文档编写。
>   - 本文档旨在为开发者、研究人员和学生提供 ChatECNU 大模型的详细使用指南，帮助用户快速上手并充分利用其功能。

## 目录

[TOC]

---

## 1. **引言**

### 1.1 背景介绍

**ChatECNU 大模型**是由华东师范大学部署的一系列 AI 大模型，旨在为开发者、研究人员和学生提供强大的自然语言处理（NLP）和多模态能力。据已知信息部署模型基于 [Qwen](https://chat.qwenlm.ai/) 和 [DeepSeek](https://www.deepseek.com/) 系列大模型，能够处理复杂的语言任务，如文本生成、翻译、代码辅助、多模态对话等。通过开放的API接口，用户可以轻松地将这些能力集成到自己的应用程序、工具或系统中。最重要的是，==提供的所有 API 对于华师大学生免费==（但<u>仅华师大学生有权限获取 Key</u>）。

ChatECNU大模型的API具有广泛的应用潜力，特别是在以下领域：

- **多模态交互**：支持文本、图像等多种模态的输入和输出，适用于智能聊天机器人、虚拟助手等场景。
- **翻译**：提供高质量的实时翻译功能，支持多种语言，适用于跨语言交流、文档翻译等场景。
- **编程辅助**：帮助开发者提高编程效率，提供代码补全、错误检测、代码解释等功能。
- **教育科研**：支持学术论文阅读、知识问答、数据分析等任务，助力科研与学习。

通过ChatECNU大模型API，用户可以快速构建智能化的应用，提升工作效率和学习体验。

### 1.2 文档说明

1. **文档来源**

   - 本文档主要基于 [华东师范大学开发者平台](https://developer.ecnu.edu.cn/vitepress/llm/model.html) 提供的 ChatECNU 大模型及其 API 文档编写。其余参考文档见 第九章参考列表。

   - 文档内容涵盖 ChatECNU 大模型的功能介绍、API 调用方法、使用场景及配置指南，旨在帮助用户更好地理解和使用 ChatECNU 大模型。


2. **文档目的**

   - 本文档旨在为开发者、研究人员和学生提供 ChatECNU 大模型的详细使用指南，帮助用户快速上手并充分利用其功能。

   - 通过本文档，用户可以了解如何通过 ChatECNU 大模型实现多模态对话、实时翻译、编程辅助等功能，并将其应用于教育、科研、日常交流等场景。


3. **免责声明**

   - 本文档仅用于知识分享和技术交流，不承担任何因使用 ChatECNU 大模型及其 API 导致的直接或间接责任。

   - 用户在使用 ChatECNU 大模型时，应遵守相关法律法规和开发者协议，确保数据的合法性和隐私安全。

   - 华东师范大学开发者平台保留对 ChatECNU 大模型及其 API 的最终解释权和修改权。


4. **技术支持**

   - 如果在使用 ChatECNU 大模型或本文档时遇到问题，请参考 [华东师范大学开发者平台](https://developer.ecnu.edu.cn/vitepress/llm/model.html) 的相关文档。

   - 如需进一步的技术支持，请联系华东师范大学开发者平台的技术团队。


5. **文档编写**

   - 本文档采用 ChatECNU 大模型辅助编写，结合了开发者平台的官方文档和实际使用经验。

   - 文档内容会随着 ChatECNU 大模型的更新迭代而不断完善。


---

## 2. **ChatECNU 大模型概述**

### 2.1 基本使用方法

ChatECNU大模型提供了便捷的在线使用方式，用户可以直接通过网页访问并使用其多模态对话功能。

- 直接访问 [chat.ecnu.edu.cn/html/#/chat](https://chat.ecnu.edu.cn/html/#/chat) 进入ChatECNU大模型的在线对话界面。
- 通过华东师范大学数据库网站访问，可以点击网站右侧的链接进入该页面。

<img src="https://northpicture.oss-cn-shanghai.aliyuncs.com/img/202503102057991.png" alt="image-20250310205734764" style="zoom:15%;" />



<img src="https://northpicture.oss-cn-shanghai.aliyuncs.com/img/202503102058351.png" alt="image-20250310205816950" style="zoom:15%;" />

### 2.2 模型列表

ChatECNU大模型提供了多种模型，以满足不同场景的需求。以下是目前支持的模型列表及其详细信息：

| 模型                 | 模型简介                                         | 上下文 | 默认限流           |
| :------------------- | :----------------------------------------------- | :----- | :----------------- |
| ecnu-reasoner        | 支持思维链的深度思考模型                         | 64K    | rpm=30 , rpd=1000  |
| ecnu-max             | 更强的推理能力，支持联网搜索                     | 8K     | rpm=30, rpd=1000   |
| ecnu-plus            | 通用的推理能力，更稳定的输出                     | 32K    | rpm=120 ，rpd=5000 |
| ecnu-vl              | 支持多模态理解的对话模型                         | 32K    | rpm=30 , rpd=1000  |
| ecnu-embedding-small | 通用文本向量能力，1024 维                        | 8K     | rpm=600            |
| ecnu-rerank          | 通用文本重排序                                   | 8K     | rpm=600            |
| ecnu-image           | 通用的文生图                                     | 1K     | rpm=30, rpd=1000   |
| gpt-4                | 兼容 gpt-4 的模型配置，实际模型与 ecnu-plus 相同 | 32K    | rpm=120，rpd=5000  |
| ChatECNU             | 历史兼容，实际模型与 ecnu-plus 相同              | 32K    | rpm=120，rpd=5000  |

**模型使用建议**：

- 对于需要深度推理的任务（如复杂问题解答），建议使用 **ecnu-reasoner**。
- 对于多模态任务（如图像+文本对话），建议使用 **ecnu-vl**。
- 对于通用对话任务，建议使用 **ecnu-plus** 或 **ChatECNU**。

### 2.3 令牌获取

为了使用 ChatECNU 大模型的 API 服务，用户需要获取个人令牌（Token）。令牌是用户身份的唯一标识，用于验证 API 请求的合法性。以下是获取令牌的详细步骤：

1. **访问ChatECNU在线对话界面**：
   - 打开浏览器，访问 [chat.ecnu.edu.cn/html/#/chat](https://chat.ecnu.edu.cn/html/#/chat)。
2. **登录账号**：
   - 如果尚未登录，请使用华东师范大学的统一身份认证账号登录系统。
3. **进入令牌管理页面**：
   - 在页面左下角找到并点击**头像**。
   - 在弹出的菜单中选择**“我的令牌”**选项。
4. **获取个人令牌**：
   - 1在“我的令牌”页面中，系统会显示您的个人令牌（Key）。
   - 点击“复制”按钮，将令牌保存到剪贴板。

<img src="https://northpicture.oss-cn-shanghai.aliyuncs.com/img/202503102100524.png" alt="image-20250310210011147" style="zoom:15%;" />

<img src="https://northpicture.oss-cn-shanghai.aliyuncs.com/img/202503102141940.png" alt="image-20250310214100815" style="zoom:33%;" />

---

## 3. **大模型多模态对话应用：ChatBox**

### 3.1 功能介绍

ChatBox 是一个功能强大的 AI 模型桌面客户端，支持多模态（文本、图像等）的交互式聊天。它不仅兼容主流的 AI 模型（如 ChatGPT、Claude、Google Gemini 等），还支持本地模型的访问（如 llama2、Mistral 等），适用于 Windows、Mac、Linux、Web、Android 和 iOS 全平台。以下是 ChatBox 的主要特性：

- **本地数据存储**：
  - 您的数据保留在您的设备上，确保数据永不丢失并保护您的隐私。
- **无需部署、直接安装的安装包**：
  - 通过可下载的安装包快速开始使用，无需复杂设置。
- **支持多个 LLM 提供商**：
  - 无缝集成多种 AI 模型，包括：
    - OpenAI (ChatGPT)
    - Azure OpenAI
    - Claude
    - Google Gemini Pro
    - Ollama（支持本地模型，如 llama2、Mistral、Mixtral、codellama、vicuna、yi 和 solar）
    - ChatGLM-6B
  - **ChatECNU** 提供 OpenAI 兼容的接口，因此也可以通过 ChatBox访问。
- **使用 Dall-E-3 生成图像**：
  - 使用 Dall-E-3 创建您想象中的图像。
- **增强提示**：
  - 高级提示功能，精炼并聚焦您的查询以获得更好的响应。
- **键盘快捷键**：
  - 使用快捷键加速您的工作流程，保持高效。
- **Markdown、Latex 和代码高亮**：
  - 使用 Markdown 和 Latex 的全部功能生成消息，并结合各种编程语言的语法高亮，提高可读性和呈现效果。
- **提示库和消息引用**：
  - 保存和组织提示以供重复使用，并引用消息以在讨论中提供上下文。
- **流式回复**：
  - 通过即时、渐进式回复快速响应您的互动。
- **人体工程学 UI 和深色主题**：
  - 用户友好的界面，带有夜间模式选项，减少长时间使用时的眼睛疲劳。
- **团队协作**：
  - 轻松协作并在团队中共享 OpenAI API 资源。[了解更多](https://github.com/Bin-Huang/chatbox/blob/main/team-sharing/README.md)
- **跨平台可用性**：
  - 支持 Windows、Mac、Linux、Web、iOS 和 Android 全平台。
- **多语言支持**：
  - 提供多种语言支持，包括：
    - English
    - 简体中文 (Simplified Chinese)
    - 繁體中文 (Traditional Chinese)
    - 日本語 (Japanese)
    - 한국어 (Korean)
    - Français (French)
    - Deutsch (German)
    - Русский (Russian)

- 更多详细信息，请参考 [ChatBox 文档]([chatboxai.app](https://chatboxai.app/zh))。


### 3.2 使用场景

ChatBox 的多模态聊天功能适用于多种场景，以下是一些典型的使用场景：

1. **教育**：
   - 学生可以通过 ChatBox 与 AI 模型进行互动，解答学术问题、生成学习资料或进行语言翻译。
   - 教师可以使用 ChatBox 生成教学材料、设计课程内容或进行课堂互动。

2. **科研**：
   - 研究人员可以利用 ChatBox 进行文献阅读、数据分析、代码生成等任务。
   - 通过多模态功能，ChatBox 还可以帮助处理图像数据或生成科研报告。

3. **日常交流**：
   - 用户可以通过 ChatBox 进行智能对话、生成创意内容或进行多语言翻译。
   - 支持图像生成功能，用户可以根据文本描述生成个性化的图像。

4. **编程辅助**：
   - 开发者可以使用 ChatBox 生成代码片段、调试程序或学习新的编程语言。
   - 支持代码高亮和 Markdown 渲染，提升代码的可读性和呈现效果。

### 3.3 配置方法

ChatBox 支持与 ChatECNU 大模型的集成，特别是 **ecnu-vl 模型**，该模型支持多模态理解（文本和图像）。以下是使用 ecnu-vl 模型实现多模态对话的技术实现步骤：

1. **安装 ChatBox**：
   - 访问 [Chatbox AI官网：办公学习的AI好助手，全平台AI客户端，官方免费下载](https://chatboxai.app/zh) 下载适合您操作系统的安装包。
   - 安装完成后，启动 ChatBox 并登录您的账号。
2. **配置 ChatECNU 大模型**：
   - 在 ChatBox 的设置中，选择“添加模型”并输入 ChatECNU 大模型的 API 地址和令牌。
   - 选择所需的模型（以 **ecnu-vl 模型** 为例）作为默认模型。
   - API 域名：https://chat.ecnu.edu.cn/open/api/v1
   - API 路径：chat/completions
3. **发送多模态请求**：
   - 在 ChatBox 的输入框中，输入文本或上传图像。
   - 点击“发送”按钮，ChatBox 会将请求发送到 ChatECNU 大模型，并返回多模态响应。



<img src="https://northpicture.oss-cn-shanghai.aliyuncs.com/img/202503102128734.png" alt="image-20250310212821521" style="zoom:15%;" />



<img src="https://northpicture.oss-cn-shanghai.aliyuncs.com/img/202503102137256.png" alt="image-20250310213720094" style="zoom: 33%;" />

---

## 4. **随时调用的翻译软件：sTranslate**

### 4.1 功能介绍

sTranslate 是一款功能强大的翻译工具，支持实时翻译和浏览器沉浸式翻译，适用于多种语言和场景。以下是 sTranslate 的主要功能：

1. **实时翻译**：
   - 支持多种翻译语言，覆盖全球主流语言。
   - 提供多种翻译方式，包括：
     - **输入翻译**：直接输入文本进行翻译。
     - **划词翻译**：选中文本后自动翻译。（==配合快捷键非常方便==）
     - **截图翻译**：通过截图识别文本并翻译。
     - **剪贴板翻译**：自动翻译剪贴板中的内容。
     - **鼠标划词翻译**：鼠标选中文本后实时翻译。
   - 支持同时显示多个翻译服务的结果，方便用户比较和选择最合适的翻译。
2. **OCR（光学字符识别）**：
   - 支持中、英、日、韩等多种语言的离线 OCR，基于 PaddleOCR，识别效果优秀且反应迅速。
   - 支持截图 OCR、剪贴板 OCR 和文件 OCR。
   - 支持静默 OCR，用户无需手动操作即可完成识别。
   - 同时支持微信、百度、腾讯、OpenAI、Google 等第三方 OCR 服务。
3. **多翻译服务支持**：
   - 支持接入 OpenAI、Gemini、ChatGLM、百度、微软、腾讯、有道、阿里等十多家翻译服务。
   - 提供免费 API 供用户选择，满足不同场景的需求。
4. **特色功能**：
   - **回译**：将翻译结果再次翻译回原文，帮助用户验证翻译准确性。
   - **全局 TTS（文本转语音）**：支持将翻译结果转换为语音播放。
   - **写作辅助**：选中文本后直接翻译并替换内容，提升写作效率。
   - **自定义 Prompt**：用户可以根据需求自定义翻译提示。
   - **二维码识别**：支持识别二维码内容。
   - **外部调用**：支持通过命令行或 API 调用 sTranslate 的功能。

更多详细信息，请参考 [sTranslate 文档](https://github.com/ZGGSONG/STranslate/blob/main/README_ZH.md) 和 [sTranslate 使用说明](https://stranslate.zggsong.com/docs/)。

### 4.2 使用场景

sTranslate 的实时翻译和浏览器沉浸式翻译功能适用于多种场景，以下是一些典型的使用场景：

1. **文档翻译**：
   - 用户可以通过 sTranslate 快速翻译外文文档，支持多种文件格式（如 PDF、Word 等）。
   - 支持 OCR 功能，可以直接识别扫描件或图片中的文字并进行翻译。
2. **跨语言交流**：
   - 在跨语言会议或聊天中，用户可以使用 sTranslate 进行实时翻译，打破语言障碍。
   - 支持划词翻译和剪贴板翻译，方便用户在阅读外文内容时快速获取翻译结果。
3. **学术论文阅读**：
   - 研究人员可以使用 sTranslate 翻译外文学术论文，支持专业术语的准确翻译。
   - 浏览器沉浸式翻译功能可以帮助用户快速理解外文网页内容。
4. **日常学习与工作**：
   - 学生可以使用 sTranslate 翻译外文教材或学习资料。
   - 职场人士可以使用 sTranslate 翻译邮件、报告等文档，提升工作效率。

### 4.3 配置方法

以下是配置和使用 sTranslate 的详细步骤：

1. **安装 sTranslate**：

   - 访问 [STranslate | 下载](https://stranslate.zggsong.com/download.html) 下载适合您操作系统的安装包。
   - 安装完成后，启动 sTranslate。

2. **配置翻译服务**：

   - 在 sTranslate 的设置中，选择“翻译服务”并添加 ChatECNU 翻译引擎。

   - 输入相应的模型和 API 令牌以启用翻译服务。

   - 接口：https://chat.ecnu.edu.cn/open/api/v1/chat/completions

     <img src="https://northpicture.oss-cn-shanghai.aliyuncs.com/img/202503102253531.png" alt="image-20250310225352374" style="zoom:25%;" />

3. **配置 OCR 服务**：

   - 在 sTranslate 的设置中，选择“OCR 服务”并添加 ChatECNU OCR 引擎。

   - 输入相应的模型和 API 令牌以启用翻译服务（必须使用多模态模型）。

   - 接口：https://chat.ecnu.edu.cn/open/api/v1/chat/completions

     <img src="https://northpicture.oss-cn-shanghai.aliyuncs.com/img/202503102200679.png" alt="image-20250310220056561" style="zoom:25%;" />

4. **使用实时翻译**：

   - 通过快捷键调用输入翻译、划词翻译、截图翻译等，sTranslate 将自动显示翻译结果。

5. **使用 OCR 功能**：

   - 在 sTranslate 主界面，选择“OCR”功能。
   - 通过快捷键调用 OCR 功能，sTranslate 将自动识别文本并显示识别结果，用户可以选择翻译识别后的文本。

---

## 5. **浏览器无感翻译：沉浸式翻译**

### 5.1 功能介绍

沉浸式翻译是一款功能强大的浏览器插件，支持网页翻译、PDF 翻译、视频字幕翻译、EPUB 翻译、图片翻译等多种功能，旨在为用户提供无缝的双语阅读体验。以下是沉浸式翻译的主要功能：

1. **网页翻译**：
   - 通过智能识别网页主内容区域，提供双语对照翻译，降低对原网页的“侵入性”。
   - 支持 10 余种翻译引擎，包括 DeepL、OpenAI (ChatGPT)、Google 翻译等，是支持翻译引擎最多的网页翻译插件。
2. **视频字幕翻译**：
   - 支持 YouTube、Netflix、Udemy 等 60 多个主流视频网站的实时双语字幕翻译。
   - 原汁原味的外语语音配合母语原文/译文双语对照字幕，帮助用户理解视频内容并学习外语。
3. **PDF 翻译**：
   - 在浏览器插件中提供免费的 PDF 翻译功能，保留原文档排版。
   - 支持下载单译文或原文/译文双语对照版本的 PDF。
   - 针对复杂 PDF 文件（如学术论文、商业合同），提供 [PRO 版本的 PDF 翻译](https://app.immersivetranslate.com/pdf-pro/)，支持 AI 驱动的解析技术，确保公式、图表等内容的准确翻译。
4. **EPUB 翻译**：
   - 支持将外语 EPUB 电子书翻译为双语版或单目标语言版，兼容各类电子书阅读器。
   - 用户可以将 AO3 等平台的作品导出为 EPUB 文件，翻译后导入 Kindle 阅读，享受沉浸式双语阅读体验。
5. **图片翻译**：
   - 支持翻译网页上的任何图片（如社交媒体截图、信息图表）。
   - 通过 OCR 识别和 Inpaint 技术，完美还原原始图片的视觉设计，让翻译文本自然融入图片布局。
6. **AI 智能上下文翻译**：
   - 基于 AI 技术，先理解全文语境和专业术语再进行翻译，提供更准确的翻译结果。
   - 支持文章类网页、电子书、PDF Pro 及双语字幕等多种内容形式（目前处于 Beta 阶段，仅向 Pro 会员开放）。
7. **鼠标悬停翻译**：
   - 将鼠标停留在网页段落上，按下快捷键（如 Ctrl），即可显示该段落的译文。
   - 保留段落上下文，帮助用户更好地理解外语内容。
8. **输入框翻译**：
   - 在网页输入框中输入文本后，快速连按 3 次空格键，即可将文本翻译为目标语言。
   - 适用于搜索、写作、对话等场景，无需跳出当前页面。

更多详细信息，请访问 [沉浸式翻译官网](https://immersivetranslate.com/zh-Hans/) 或 [Microsoft Edge 插件页面](https://microsoftedge.microsoft.com/addons/detail/沉浸式翻译-网页翻译插件-pdf翻译-/amkbmndfnliijdhojkpoglbnaaahippg?utm_source=official)。

### 5.2 使用场景

沉浸式翻译适用于多种场景，以下是一些典型的使用场景：

1. **学术研究**：
   - 翻译外文学术论文、PDF 文档，保留原文排版和公式、图表等内容。
   - 使用 AI 智能上下文翻译功能，确保专业术语的准确性。
2. **在线学习**：
   - 翻译 YouTube、Netflix 等平台的视频字幕，帮助用户理解外语课程。
   - 将外语 EPUB 电子书翻译为双语版，导入 Kindle 阅读。
3. **日常浏览**：
   - 翻译外文新闻、博客、社交媒体内容，提升阅读体验。
   - 使用鼠标悬停翻译功能，快速理解网页段落内容。
4. **商务办公**：
   - 翻译多语言商业合同、报告等 PDF 文档，确保格式和内容的准确性。
   - 使用输入框翻译功能，快速完成跨语言沟通。
5. **娱乐休闲**：
   - 翻译外文小说、漫画等 EPUB 电子书，享受双语阅读乐趣。
   - 翻译社交媒体截图、信息图表等内容，轻松理解外语图片信息。

### 5.3 配置方法

以下是配置和使用沉浸式翻译的详细步骤：

1. **安装插件**：

   - 访问 [沉浸式翻译官网](https://immersivetranslate.com/zh-Hans/) 或 [Microsoft Edge 插件页面](https://microsoftedge.microsoft.com/addons/detail/沉浸式翻译-网页翻译插件-pdf翻译-/amkbmndfnliijdhojkpoglbnaaahippg?utm_source=official)。
   - 点击“安装”按钮，将插件添加到浏览器中。

2. **配置翻译引擎**：

   - 打开沉浸式翻译插件，进入设置页面。
   - 点击“添加 OpenAI 兼容服务”。
   - 输入相应的 API 接口、模型和 Key 以启用翻译服务。
     - API 接口：https://chat.ecnu.edu.cn/open/api/v1/chat/completions

   <img src="https://northpicture.oss-cn-shanghai.aliyuncs.com/img/202503102206761.png" alt="image-20250310220623654" style="zoom: 25%;" />

   <img src="https://northpicture.oss-cn-shanghai.aliyuncs.com/img/202503102206554.png" alt="image-20250310220658399" style="zoom:25%;" />

3. **使用网页翻译**：

   - 打开需要翻译的外文网页。
   - 点击浏览器右上角的沉浸式翻译图标，选择“翻译网页”。
   - 插件将自动识别网页内容并显示双语对照翻译。

4. **使用 PDF 翻译**：

   - 打开需要翻译的 PDF 文件。
   - 点击沉浸式翻译图标，选择“翻译 PDF”。
   - 选择下载单译文或双语对照版本的 PDF。

5. **使用视频字幕翻译**：

   - 打开 YouTube、Netflix 等视频网站。
   - 播放视频后，插件将自动显示双语字幕。

6. **使用鼠标悬停翻译**：

   - 在网页上选中需要翻译的段落。
   - 按下快捷键（如 Ctrl），插件将显示该段落的译文。

7. **使用输入框翻译**：

   - 在网页输入框中输入文本。
   - 快速连按 3 次空格键，插件将自动翻译文本。

---

## 6. **VSCode 辅助编程：Cline**

### 6.1 功能介绍

**Cline** 是一款基于 AI 的编程助手，能够与你的 **CLI** 和 **编辑器** 无缝集成，帮助开发者高效完成复杂的软件开发任务。Cline 可以创建和编辑文件、探索大型项目、使用浏览器、执行终端命令，甚至通过 Model Context Protocol (MCP) 创建新工具来扩展自身能力。Cline 提供了一个安全且交互式的 GUI，允许用户在每个文件更改和终端命令执行前进行批准，确保开发过程的安全性和可控性。

以下是 Cline 的核心功能：

1. **任务处理**：
   - 输入任务描述或上传图像，Cline 可以将其转换为功能应用程序或通过截图修复错误。
   - Cline 会分析文件结构和源代码 AST，运行正则表达式搜索，并阅读相关文件以理解项目上下文。
2. **文件操作**：
   - 创建和编辑文件，监控 linter/编译器错误，主动修复诸如缺少导入和语法错误等问题。
   - 所有更改都会记录在文件时间轴中，方便用户跟踪和恢复修改。
3. **终端命令执行**：
   - 直接在终端中执行命令并监控输出，例如安装包、运行构建脚本、部署应用程序等。
   - 支持长时间运行的进程（如开发服务器），Cline 可以在后台运行任务时继续工作。
4. **浏览器交互**：
   - 启动无头浏览器，点击元素、输入文本、滚动页面，并捕获截图和控制台日志。
   - 适用于交互式调试、端到端测试以及修复视觉错误和运行时问题。
5. **工具扩展**：
   - 通过 Model Context Protocol (MCP)，Cline 可以创建和安装自定义工具，例如获取 Jira 工单、管理 AWS EC2 实例或获取 PagerDuty 事件。
   - 这些工具将成为 Cline 工具包的一部分，供未来任务使用。
6. **上下文管理**：
   - 支持通过 `@url`、`@problems`、`@file`、`@folder` 等方式添加上下文，优化任务处理效率。
   - 例如，粘贴 URL 以获取最新文档，或添加工作区错误和警告供 Cline 修复。
7. **检查点与恢复**：
   - 在任务完成时，Cline 会拍摄工作区快照，用户可以通过“比较”按钮查看差异，并通过“恢复”按钮回滚到特定检查点。
8. **多模型支持**：
   - 支持 OpenRouter、Anthropic、OpenAI、Google Gemini、AWS Bedrock、Azure 和 GCP Vertex 等 API 提供商。
   - 用户还可以通过 LM Studio 或 Ollama 使用本地模型。
   - 关键是**支持 OpenAI 兼容接口**，因此可以使用 ChatECNU API，而另一款类似插件 Continue 截至编写文档时仍不支持。

### 6.2 使用场景

Cline 适用于多种开发场景，以下是一些典型的使用场景：

1. **代码生成与优化**：
   - 通过自然语言描述生成代码片段，或优化现有代码以提高性能。
   - 例如：“将这段代码重构为更高效的形式”。
2. **错误修复与调试**：
   - 自动修复编译时错误（如缺少导入、语法错误）和运行时错误。
   - 通过浏览器交互功能，修复视觉错误和交互问题。
3. **项目探索与文档生成**：
   - 分析大型项目的文件结构和源代码，生成项目文档或代码注释。
   - 例如：“为这个函数生成文档”。
4. **自动化任务**：
   - 执行终端命令，自动化安装依赖、运行测试、部署应用程序等任务。
   - 例如：“运行测试并生成报告”。
5. **工具扩展与集成**：
   - 创建自定义工具，集成到开发工作流中，例如获取 Jira 工单或管理云资源。
   - 例如：“添加一个获取 Jira 工单的工具”。
6. **跨平台开发**：
   - 支持在 VS Code 和 JetBrains 系列 IDE 中使用，提供统一的开发体验。

### 6.3 配置方法

以下是配置和使用 Cline 的详细步骤：

1. **安装 Cline 插件**：

   - 打开 VS Code，进入扩展市场（Extensions）。
   - 搜索“Cline”并点击安装。

   <img src="https://northpicture.oss-cn-shanghai.aliyuncs.com/img/202503102240767.png" alt="image-20250310224031602" style="zoom:25%;" />

2. **配置 AI 模型**：

   - 打开 Cline 插件，进入设置页面。

   - 选择所需的 AI Provider（OpenAI Compatible）。

   - 输入相应的 API URL或令牌以启用模型。

     - API URL：https://chat.ecnu.edu.cn/open/api/v1/

     - Model ID：ecnu-max

     - Custom Instructions 参考：

       ```
       "You are an AI programming assistant. Your primary goal is to help the user write, debug, and optimize code. You should provide clear, concise, and accurate responses related to programming tasks. When asked about code, always assume the user is working in a professional software development environment. If the user's request is ambiguous, ask clarifying questions to ensure you provide the most relevant assistance. Focus on providing code snippets, debugging tips, performance optimization, and best practices in software development. Avoid providing non-programming related content unless explicitly asked."
       ```

       <img src="https://northpicture.oss-cn-shanghai.aliyuncs.com/img/202503102244480.png" alt="image-20250310224444320" style="zoom:25%;" />

   

3. **使用任务处理功能**：

   - 在 Cline 面板中输入任务描述，例如“修复这个函数的运行时错误”。
   - Cline 将分析代码并生成修复方案，用户可以在差异视图中查看和批准更改。

4. **执行终端命令**：

   - 在 Cline 面板中输入命令，例如“安装依赖并启动开发服务器”。
   - Cline 将在终端中执行命令并监控输出。

5. **使用浏览器交互功能**：

   - 在 Cline 面板中输入任务，例如“测试应用程序并修复视觉错误”。
   - Cline 将启动浏览器，执行测试并生成修复方案。

6. **创建自定义工具**：

   - 在 Cline 面板中输入“添加一个工具”，例如“添加一个获取 Jira 工单的工具”。
   - Cline 将创建并安装工具，供未来任务使用。

7. **添加上下文**：

   - 使用 `@url`、`@problems`、`@file`、`@folder` 等方式添加上下文，优化任务处理效率。
   - 例如，粘贴 URL 以获取最新文档，或添加工作区错误和警告供 Cline 修复。

8. **检查点与恢复**：

   - 在任务完成时，使用“比较”按钮查看快照和当前工作区的差异。
   - 使用“恢复”按钮回滚到特定检查点。

---

## 7. **API 调用示例与代码片段**

ECNU 大语言模型平台提供的所有 API 都遵循 openai 规范。您可以直接使用任意兼容 `openai` 的第三方库来调用 ECNU 大语言模型平台的 API。

注意当 API 中包含了我们自定义的能力扩展时（例如 ecnu-max 所支持的联网检索能力），`openai` 库不会处理这些扩展字段，但不影响其他部分的使用。

示例代码如下：

```python
import os
from openai import OpenAI
import requests

# 使用 OpenAI SDK 调用 ECNU 大语言模型平台的函数
def call_openai_sdk(api_key, base_url, model, messages):
    # 创建 OpenAI 客户端
    client = OpenAI(
        api_key=api_key,  # API 密钥
        base_url=base_url,  # 基础 URL
    )
    # 创建聊天完成请求
    completion = client.chat.completions.create(
        model=model,  # 模型名称
        messages=messages,  # 消息列表
    )
    # 返回 JSON 格式的响应
    return completion.model_dump_json()

# 直接调用 ECNU 大语言模型平台 API 的函数
def call_api_directly(api_key, url, model, messages, search_mode=None):
    # 设置请求头
    headers = {
        "Authorization": f"Bearer {api_key}",  # 认证信息
        "Content-Type": "application/json"  # 内容类型
    }

    # 设置请求数据
    data = {
        "model": model,  # 模型名称
        "messages": messages  # 消息列表
    }

    # 如果启用了搜索模式，则添加到请求数据中
    if search_mode:
        data["search_mode"] = search_mode

    # 发送 POST 请求
    response = requests.post(url, headers=headers, json=data)
    # 返回 JSON 格式的响应
    return response.json()

# 示例调用
if __name__ == "__main__":
    api_key = 'your-api-key'  # API 密钥
    base_url = "https://chat.ecnu.edu.cn/open/api/v1"  # 基础 URL
    model = "ecnu-plus"  # 模型名称
    messages = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},  # 系统消息
        {'role': 'user', 'content': '你是谁？'}  # 用户消息
    ]

    # 调用使用 OpenAI SDK 的函数并打印结果
    print(call_openai_sdk(api_key, base_url, model, messages))

    url = "https://chat.ecnu.edu.cn/open/api/v1/chat/completions"  # API URL
    model = "ecnu-max"  # 模型名称
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},  # 系统消息
        {"role": "user", "content": "华东师范大学是哪一年成立的？"}  # 用户消息
    ]
    search_mode = "enable"  # 启用搜索模式

    # 调用直接调用 API 的函数并打印结果
    print(call_api_directly(api_key, url, model, messages, search_mode))
```

---

## 8. **API 调用注意事项**

在使用ChatECNU大模型API时，为了确保服务的稳定性和高效性，请务必注意以下事项：

### 1. API调用规范

- **避免并行调用**：
  - 建议等待上一个API请求的响应结束后再发起下一个请求，以避免服务器过载。
  - 并行调用可能导致请求失败或响应延迟。
- **遵守限流策略**：
  - 每个模型都有默认的限流策略（如rpm和rpd），请确保您的调用频率在限制范围内。
  - **rpm（每分钟请求数）**：表示每分钟允许的最大请求数。
  - **rpd（每天请求数）**：表示每天允许的最大请求数。
  - 如果超出限流，请求可能会被拒绝或延迟处理。
- **合理使用上下文长度**：
  - 不同模型的上下文长度不同（如ecnu-reasoner支持64K，ecnu-max支持8K）。
  - 请根据任务需求选择合适的模型，并确保输入内容不超过模型的上下文长度限制。

### 2. 重要变更

- **`ecnu-max` 停止支持联网搜索功能**：
  - 由于模型架构升级调整，`ecnu-max` 将于近期停止支持联网搜索功能。
  - 如果您的业务依赖 `ecnu-max` 的联网搜索能力，请尽快切换到其他解决方案。
  - 更多详情请参考：[重要变更](https://developer.ecnu.edu.cn/vitepress/llm/model.html#重要变更)。

### 3. Prompt工程指南

- **优化输入提示（Prompt）**：

  - 合理的Prompt设计可以显著提升模型的输出质量。
  - 建议参考[Prompt工程指南](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html)，了解如何编写高效的Prompt。

- **示例**：

  - 对于翻译任务，可以明确指定源语言和目标语言：

    ```
    将以下英文翻译为中文：Hello, how are you?
    ```

  - 对于代码生成任务，可以提供清晰的上下文：

    ```
    编写一个Python函数，计算两个数的和。
    ```

### 4. 开发者协议

- **遵守开发者协议**：
  - 使用ChatECNU大模型API时，请务必遵守[ChatECNU大模型服务开发者协议](https://developer.ecnu.edu.cn/vitepress/llm/tos.html)。
  - 协议中包含了API使用的法律责任、数据隐私保护等内容，请仔细阅读并遵守。
- **禁止滥用API**：
  - 禁止将API用于违法、违规或不道德的用途。
  - 禁止通过API生成或传播虚假信息、恶意内容等。

### 5. 数据隐私与安全

- **保护用户数据**：
  - 请勿通过API传输敏感信息（如个人隐私、密码等）。
  - 确保您的应用符合相关数据隐私法规（如GDPR、网络安全法等）。
- **日志记录**：
  - 建议记录API调用的请求和响应日志，以便排查问题和优化性能。
  - 注意日志中不要包含敏感信息。

### 6. 模型更新与兼容性

- **模型更新**：
  - 模型会根据学校的算力资源和用户需求不断更新迭代，同时承诺保持兼容性。
  - 用户可以通过[华东师范大学开发者平台](https://developer.ecnu.edu.cn/vitepress/llm/model.html)获取最新的模型信息和开发文档。
- **兼容性**：
  - 在模型更新后，API接口会尽量保持向后兼容，但仍建议定期查看开发者平台以了解最新动态。

### 7. 令牌管理与安全

- **令牌的安全性**：
  - 令牌是您访问API的凭证，请妥善保管，避免泄露。
  - 如果令牌泄露，请及时在“我的令牌”页面中重新生成新令牌。
  - 使用包括但不限于本文提及的第三方工具时，请确保其隐私政策符合您的需求，避免敏感数据泄露。
- **令牌的有效期**：
  - 令牌通常具有较长的有效期，但如果长时间未使用，可能会失效。如果遇到令牌失效的情况，请重新获取新令牌。
- **令牌的权限**：
  - 令牌与您的账号权限绑定，确保您的账号具有调用API的权限。如果遇到权限问题，请联系系统管理员。
- **问题反馈**：
  - 如果在获取或使用令牌时遇到问题，请参考[华东师范大学开发者平台](https://developer.ecnu.edu.cn/vitepress/llm/model.html)的相关文档或联系技术支持。

---

## 9. **参考列表**

- [华东师范大学开发者平台](https://developer.ecnu.edu.cn/vitepress/llm/model.html)
- [chatbox/doc/README-CN.md at main · Bin-Huang/chatbox](https://github.com/Bin-Huang/chatbox/blob/main/doc/README-CN.md)
- [chatboxai.app](https://chatboxai.app/zh)
- [STranslate/README_ZH.md at main · ZGGSONG/STranslate](https://github.com/ZGGSONG/STranslate/blob/main/README_ZH.md)
- [STranslate | 使用说明](https://stranslate.zggsong.com/docs/)
- [沉浸式翻译 - 双语对照网页翻译插件 | PDF翻译 | 视频字幕翻译](https://immersivetranslate.com/zh-Hans/)
- [cline/locales/zh-cn/README.md at main · cline/cline](https://github.com/cline/cline/blob/main/locales/zh-cn/README.md)