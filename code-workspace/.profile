# ~/.profile: executed by Bourne-compatible login shells.

if [ "$BASH" ]; then
  if [ -f ~/.bashrc ]; then
    . ~/.bashrc
  fi
fi

mesg n 2> /dev/null || true

# Created by `pipx` on 2025-02-18 20:03:14
export PATH="$PATH:/config/.local/bin"
