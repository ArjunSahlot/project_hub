#!/bin/bash

download_link=https://github.com/ArjunSahlot/project_hub/archive/master.zip
temporary_dir=$(mktemp -d) \
&& curl -LO $download_link \
&& unzip -d $temporary_dir master.zip \
&& rm -rf master.zip \
&& mv $temporary_dir/project_hub-master $1/project_hub \
&& rm -rf $temporary_dir
echo -e "[0;32mSuccessfully downloaded to $1/project_hub[0m"
