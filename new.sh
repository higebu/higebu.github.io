#!/bin/sh

TITLE=$1
SLUG=$2
DATE=$(date "+%Y-%m-%d %H:%M")
CATEGORY=$3
TAGS=$4
SUMMARY=$5

BODY="title: $TITLE
Slug: $SLUG
Date: $DATE
Category: $CATEGORY
Tags: $TAGS
Summary: $SUMMARY

## Image Tag
"

echo "${BODY}" > content/${SLUG}.md
echo '{% img [class name] /images/image-file-name [width [height]] [title text] %}' >> content/${SLUG}.md
$EDITOR "content/${SLUG}.md"
