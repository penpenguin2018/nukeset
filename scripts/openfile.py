#!coding:utf8
import nuke
import nukescripts
import os

def openfile():
	focusKnobs = ["file","vfield_file"]
	nodes = nuke.selectedNodes()
	if len(nodes) != 1:
		nuke.message("노드를 하나만 선택해주세요.")
		return
	for knob in focusKnobs:
		if knob in nodes[0].knobs():
			path = nodes[0][knob].value()
			if path == "":
				nuke.message("경로가 비어있습니다.")
				return
			parentPath = os.path.dirname(path)
			if not os.path.exists(parentPath):
				nuke.message("경로가 존재하지 않습니다.")
				return
			nukescripts.start(parentPath)
			return
	nuke.message("file Knob을 사용하는 노드가 아닙니다.")
