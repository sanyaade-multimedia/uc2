# -*- coding: utf-8 -*-
#
#	Copyright (C) 2011 by Igor E. Novikov
#	
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#	
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#	
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.


class UCMethods:

	presenter = None
	model = None

	def __init__(self, presenter):
		self.presenter = presenter
		self.model = presenter.model

	def set_doc_origin(self, origin):
		self.model.doc_origin = origin

	def delete_object(self, obj):
		parent = obj.parent
		parent.childs.remove(obj)

	def insert_object(self, obj, parent, index):
		parent.childs.insert(index, obj)
		obj.parent = parent

	def append_object(self, obj, parent):
		parent.childs.append(obj)
		obj.parent = parent

	def append_objects(self, objs, parent):
		parent.childs += objs
		for obj in objs:
			obj.parent = parent
