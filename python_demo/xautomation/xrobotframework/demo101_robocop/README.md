https://github.com/MarketSquare/robotframework-robocop
https://robocop.readthedocs.io/en/latest/
https://robot-framework.readthedocs.io/en/stable/

```sh
pip install -U robotframework-robocop

robocop --report rules_by_error_type test.robot
```

FAQ
---
<details>
  <summary>Can I integrate Robocop with my code editor (IDE)?</summary>

  **Yes**, Robocop integrates nicely with popular IDEs like PyCharm or VSCode
  thanks to [Robot Framework Language Server](https://github.com/robocorp/robotframework-lsp).
  Read simple manual (README) in that project to figure out how to install & use it.

  You can also use Robocop in PyCharm easily as an external tool.
  To configure it, go to: `File` → `Settings` → `Tools` → `External Tools`
  and click `+` icon. Then put values based on
  [official instructions](https://www.jetbrains.com/help/pycharm/configuring-third-party-tools.html)
  or this screenshot:

  ![Robocop](docs/images/robocop_external_tool.jpg)

  If you're using Python virtual environment in your project,
  make sure to provide correct path to robocop.exe located in `venv\Scripts\robocop.exe`.
  Now, you can run Robocop by right-clicking on a file or directory and choosing
  `External tools` → `Robocop`.

  We suggest also to add a keyboard shortcut (e.g. `Ctrl + , (comma)`)
  to quickly run Robocop on selected files. You can map the shortcut in `Settings` → `Keymap`.
</details>

<details>
  <summary>Can I load configuration from file?</summary>

  **Yes**, there are multiple ways to configure Robocop:

  **Argument file**

  You can add command line options to an argument file, preferably one option with value for a line.
  Such file can be used as an input for Robocop with `--argumentfile / -A` option, e.g.
  ```robocop -A robocop.cfg```. You can mix arguments from a file with ones provided in run command.

  Example argument file:

  ```commandline
  --exclude *doc*
  --exclude 0510
  --threshold W
  --configure inconsistent-assignment:assignment_sign_type:equal_sign
  --configure line-too-long:line_length:140
  --reports all
  --output robocop.log
  ```

  ---

  **`.robocop` file**

  It is a default file that is loaded only when no command line options are provided for Robocop.
  When running plain `robocop` command, it looks for `.robocop` file from place where it was run
  until it finds `.git` file. Options can be provided like in the example above.

  ---

  **`pyproject.toml` file**

  If there is no `.robocop` file and `toml` module is installed,
  Robocop will try to load configuration from `pyproject.toml` file (if it exists).
  Options have the same names as command line arguments
  and need to be placed under `[tool.robocop]` section.

  Example configuration file:

  ```commandline
  [tool.robocop]
  paths = [
      "tests\\atest\\rules\\bad-indent",
      "tests\\atest\\rules\\duplicated-library"
  ]
  include = ['W0504', '*doc*']
  exclude = ["0203"]
  reports = [
      "rules_by_id",
      "scan_timer"
  ]
  ignore = ["ignore_me.robot"]
  ext-rules = ["path_to_external\\dir"]
  filetypes = [".txt", ".tsv"]
  threshold = "E"
  format = "{source}:{line}:{col} [{severity}] {rule_id} {desc} (name)"
  output = "robocop.log"
  configure = [
      "line-too-long:line_length:150",
      "0201:severity:E"
  ]
  no_recursive = true
  ```
</details>

<details>
  <summary>I use different coding standards. Can I configure rules so that they fit my needs?</summary>

  **Yes**, some rules are configurable. You can list them by running `robocop --list-configurables`
  or just `robocop -lc`.

  Configuring is done by using `-c / --configure` command line option followed by pattern
  `<rule>:<param_name>:<value>` where:
  - `<rule>` can either be rule name or its id
  - `<param_name>` is a public name of the parameter
  - `<value>` is a desired value of the parameter

  For example:

  ```commandline
  --configure line-too-long:line_length:140
  ```

  is equivalent to

  ```commandline
  -c 0508:line_length:140
  ```

  ---
  Each rule's severity can also be overwritten. Possible values are
  `e/error`, `w/warning` or `i/info` and are case-insensitive. Example:

  ```commandline
  -c too-long-test-case:severity:e
  ```

  ---
  If there are special cases in your code that violate the rules,
  you can also exclude them in the source code.

  Example:

  ```
  Keyword with lowercased name  # robocop: disable
  ```

  More about it in
  [our documentation](https://robocop.readthedocs.io/en/stable/including_rules.html#ignore-rule-from-source-code).

</details>

<details>
  <summary>Can I define custom rules?</summary>

  **Yes**, you can define and include custom rules using `-rules / --ext-rules` command line option
  by providing a path to a file containing your rule(s). The option accepts comma-separated list
  of paths to files or directories, e.g.
  ```
  robocop -rules my/own/rule.py --ext-rules rules.py,external_rules.py
  ```

  If you feel that your rule is very helpful and should be included in Robocop permanently,
  you can always share your solution by
  [submitting a pull request](https://github.com/MarketSquare/robotframework-robocop/pulls).
  You can also share your idea by
  [creating an issue](https://github.com/MarketSquare/robotframework-robocop/issues/new/choose).

  More about external rules with code examples in
  [our documentation](https://robocop.readthedocs.io/en/stable/external_rules.html).
</details>

<details>
  <summary>Can I use Robocop in continuous integration (CI) tools?</summary>

  **Yes**, it is easy to integrate Robocop with CI and other tools.
  For more details read [our documentation](https://robocop.readthedocs.io/en/stable/ci.html).

</details>

<details>
  <summary>Can I configure return status / code?</summary>

  **Yes**, by default Robocop returns code 0 if number of found issues does not exceed quality gates.

  Quality gates are the number specified for each severity (error, warning, info) that cannot be
  exceeded. Every violation of quality gates increases the return code by 1 up to maximum of 255.
  Default values for quality gates are:

  ```
  quality_gate = {
            'E': 0,
            'W': 0,
            'I': -1
        }
  ```

  which shows the accepted number of issues by severity. In that case each error and warning
  increases the return code. Rules with INFO severity do not affect the return code.

  To configure quality gates, you simply use `-c / --configure` command line option
  with following pattern ```--configure return_status:quality_gates:<severity>=limit```.
  You can change all limits at once. Example:

  ```commandline
  --configure return_status:quality_gates:E=0:W=100:I=-1
  ```

  which means that no errors are accepted, up to 100 warnings are tolerated and issues with
  INFO severity do not affect the return code.

</details>

<details>
  <summary>What is the difference between Robocop and rflint?</summary>

  Robocop is better in every case because it:

  - has maaaaany rules that check the quality of your Robot Framework code
  - is integrated with popular IDE tools
  - is highly configurable
  - has very good defaults that work out of the box
  - can be configured in source code
  - uses the latest [Robot Framework Parsing API](https://robot-framework.readthedocs.io/en/stable/)
  - is actively developed & fixed
  - is easy to integrate with external tools
  - can redirect output to a file
  - displays nice reports
  - is easy to extend it with new rules
  - is cool :nerd_face:

  Still not convinced?
  [Watch our talk](https://www.youtube.com/watch?v=vZoyi2ObM8E)
  about Robocop &
  [Robotidy](https://github.com/MarketSquare/robotframework-tidy)
  and see for yourself! :monocle_face:

</details>