# higebu.github.io

[![Build Status](https://travis-ci.org/higebu/higebu.github.io.svg?branch=master)](https://travis-ci.org/higebu/higebu.github.io)

Source code for [www.higebu.com][1] based on [pelican][2].

# How to deploy

1. Get GitHub Access Token from [Personal access tokens page](https://github.com/settings/tokens).
2. Set `GH_TOKEN` to env vars.
3. Run following commands.

```
pip install -r requirements.txt
git submodule update --init --recursive
make travis
```

 [1]: http://www.higebu.com/
 [2]: http://docs.getpelican.com/
