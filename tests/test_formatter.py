from mkdocs_onecompiler_plugin.main import formatter

html_output = """
<iframe id="#id" class="onecompiler extra_class" frameBorder="0" src="https://onecompiler.com/embed/python?availableLanguages=true&hideLanguageSelection=false&hideNew=false&hideNewFileOption=false&disableCopyPaste=false&hideStdin=false&hideResult=false&hideTitle=false&listenToEvents=false&theme=dark" height="450px" width="100%" onload='this.contentWindow.postMessage({
        eventType: "populateCode",
        language: "python",
        files: [
            {
                "name": "untitled",
                "content": `a = 3`
            }
        ]
    }, "*");'>
</iframe>
""".strip(
    "\n"
)


def test_formatter():
    source = "a = 3"
    language = "onecompiler"
    css_class = "onecompiler"
    classes = ["extra_class"]
    id_value = "#id"
    attrs = {"lang": "python", "listenToEvents": False, "theme": "dark"}
    fmt = formatter(
        source,
        language,
        css_class=css_class,
        attrs=attrs,
        classes=classes,
        id_value=id_value,
    )

    assert fmt.strip("\n") == html_output
