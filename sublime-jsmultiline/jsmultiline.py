# Copyright 2013 William Summers, Metatribal Research
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
# 

import sublime, sublime_plugin, re
  
class JsMultilineCommand(sublime_plugin.TextCommand):  
    def run(self, edit):  
    	# iterate over each selected region
        for region in self.view.sel():
        	# if the region is not empty
            if not region.empty():  
                # get the selected text
                selectedText = self.view.substr(region)
                # escape quotes and backslashes in selected text
                newText = re.sub(r'("|\'|\\)', r'\\\1', selectedText)
                # quote the lines and add commas
                newText = re.sub(r'(.*)', r"'\1',", newText)
                # remove trailing comma
                newText = newText[:-1]
                # add the beginning and ending
                newText = "[" + newText + "].join('\\n');"

                self.view.replace(edit, region, newText) 
