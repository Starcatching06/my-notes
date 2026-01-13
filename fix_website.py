import os

# 1. 重写 mkdocs.yml (配置 MathJax)
yaml_content = r"""site_name: 机械工学僧的笔记
site_url: ""

theme:
  name: material
  language: zh
  palette: 
    - scheme: default
      toggle:
        icon: material/brightness-7 
        name: Switch to dark mode
    - scheme: slate
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.top
    - content.code.copy

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.arithmatex:
      generic: true

extra_javascript:
  - javascripts/mathjax.js
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
"""

with open("mkdocs.yml", "w", encoding="utf-8") as f:
    f.write(yaml_content)
print("✅ mkdocs.yml 重写成功！")

# 2. 确保 javascripts 目录存在
os.makedirs("docs/javascripts", exist_ok=True)

# 3. 重写 mathjax.js
js_content = r"""window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};
"""

with open("docs/javascripts/mathjax.js", "w", encoding="utf-8") as f:
    f.write(js_content)
print("✅ mathjax.js 重写成功！")
