#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2015 Timu Eren <timu.eren@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def parse(acceptLanguage):

    languages = acceptLanguage.split(',')
    _return = []
    for language in languages:
        bits = language.split(';')
        ietf = bits[0].split('-')
        _return.append(dict(lang=ietf[0].strip(),
                            quality=float(bits[1].strip().split('=')[1]) if 1 < len(bits) else 1.0,
                            region=ietf[1].strip() if 1 < len(ietf) else None))
    sorted(_return, key=lambda x: x["quality"], reverse=True)
    return _return


if __name__ == '__main__':
    print parse("fr-CA,   fr;   q=0.8,    en-US;   q=0.6,en;q=0.4,*;q=0.1")
