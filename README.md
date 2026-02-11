# To-Do Service

<!-- vale Google.Passive = NO -->
<!-- vale Google.Acronyms = NO -->
<!-- vale write-good.Passive = NO -->

REST API Sample for shared documentation practice

For the REST API docs, see [The To-Do Service docs](https://uwc2-apidoc.github.io/to-do-service-auto/).

**NOTE**:

This code is experimental and is intended for instructional use only.
Use at your own risk. No warranty of serviceability is expressed or implied.

## Contributing documentation

Feel free to contribute new documentation and improve existing the existing docs.
For more information about contributing to the project, see
[Contributing](https://uwc2-apidoc.github.io/to-do-service-auto/contributing/) in the project's documentation.
Review all the guidelines and style guide information to create a successful pull request.

### Configure your system

Before you start editing files, be sure to configure the system on which
you'll be creating or revising files as described in this section.

Your contributions must pass the automated tests on the content before they're
reviewed for acceptance. These tools help make your contribution compatible
with the automated testing.

1. Fork this repository to your own GitHub account.
2. Make sure you can build a local copy of the documentation from your fork.
3. Install [Vale](https://vale.sh/) on your development or editing computer.
   To help you have a successful pull request experience, it's also helpful
   to add these extensions if you edit in VS Code:
    * `Markdownlint` or `Markdown Essentials`, which includes `Markdownlint`.
        * Configure `Markdownlint` in VS Code to use the settings defined
            in [`.github/config/.markdownlint.jsonc`](./.github/config/.markdownlint.jsonc)
    * `Vale VSCode` and configure
        * `Vale > Enable Spellcheck`: checked
        * `Vale > ValeCLI:Config`: `.vale.ini`
        * `Vale > ValeCLI:minAlertLevel`: `inherited`
        * Leave the others as the default

4. Read the detailed [Contributor's Guide docs](https://uwc2-apidoc.github.io/to-do-service-auto/contributing/)
    for complete information about how to create and edit files.
5. Build and test your changes locally from a feature branch in your fork of the repo
    before you submit a pull request, please.
