# Puraya

## How does it work?

Puraya copies nested directories from the specified source directories list to the flat structure inside the destination directory.

**Source directory contents**

        sample1
        ├── bar
        │   ├── 1
        │   └── 2
        └── foo
            ├── 3
            └── 4

**Source directory contents**

        sample2
        ├── bad
        │   ├── 5
        │   └── 6
        └── baz
            ├── 7
            └── 8

**Destination directory contents**

        sample-flat
        ├── sample1
        │   ├── bar - 1
        │   ├── bar - 2
        │   ├── foo - 3
        │   └── foo - 4
        └── sample2
            ├── bad - 5
            ├── bad - 6
            ├── baz - 7
            └── baz - 8

## Installation

git clone https://torunar@bitbucket.org/torunar/puraya.git

## Usage

python puraya sample1 sample2 ...
