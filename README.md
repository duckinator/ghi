# ??? <!--[![Build Status][build-status-link]][build-status-img]-->

Manage GitHub issues less awkwardly.

[build-status-link]: https://api.cirrus-ci.com/github/duckinator/emanate.svg
[build-status-img]: https://cirrus-ci.com/github/duckinator/emanate

## Installation

### Via Pip/PyPi

```
$ pip3 install ???
```

<!--
### Via DNF (Fedora 29 only)

If you're on Fedora 29, the [Puppy Technology](https://puppy.technology/)
RPM repository contains the latest package for ???.

```
$ dnf install https://rpm.puppy.technology/repo.rpm
$ dnf install ??? -\-refresh
```
-->

## Configuration

To avoid errors due to hitting rate limits, GHI requires a Personal
Access Token for GitHub.

### Acquiring A Personal Access Token

To acquire a personal access token:

1. Go to: https://github.com/settings/tokens/new
2. For `Token description`, enter `ghi CLI client`.
3. Scroll to the bottom of the page.
4. Click `Generate token`. This will take you to a new page.
5. Save the token somewhere. **You can't access it again.**

### Configuration File

Make a file, `$HOME/.config/ghi/config.json`:

```
{
  "github": {
    "token": "<GITHUB TOKEN>"
  },
  "ignored": [
    "some/repository-you-dont-care-about",
    "some-other/repositoriy"
  ]
}
```

## Usage

After configuring it, just run `ghi`.

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/duckinator/emanate. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the ??? project's codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/duckinator/emanate/blob/master/CODE_OF_CONDUCT.md).
