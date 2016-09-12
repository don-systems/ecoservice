from openerp.osv import fields, osv


class project_project(osv.osv):
    _inherit = 'project.project'

    def write(self, cr, user, ids, vals, context=None):
        """
        Extends the write method to change the color of the associated tasks accordingly if the color is changed
        """
        if 'color' in vals:
            ids = ids if isinstance(ids, list) else [ids]
            task_obj = self.pool.get('project.task')
            tasks = task_obj.search(cr, user, [('project_id', 'in', ids)])
            task_obj.write(cr, user, tasks, vals={'color': vals['color']}, context=context)

        return super(project_project, self).write(cr, user, ids, vals, context=context)


class project_task(osv.osv):
    _inherit = 'project.task'
    _order = 'name'

    def create(self, cr, uid, vals, context=None):
        """
        Gets the associated project_id for the tasks and adds 'color' to the vals list
        """
        if 'project_id' in vals:
            project_obj = self.pool.get('project.project')
            project = project_obj.browse(cr, uid, vals['project_id'], context=context)
            vals['color'] = project.color

        return super(project_task, self).create(cr, uid, vals, context=context)

    def write(self, cr, user, ids, vals, context=None):
        """
        If there's a 'project_id', the function writes the 'color_id' in the vals to change the 'color_id'
         for every existing task which is associated to the project
        """
        if 'project_id' in vals:
            project_obj = self.pool.get('project.project')
            project = project_obj.browse(cr, user, vals['project_id'], context=context)
            vals['color'] = project.color
        return super(project_task, self).write(cr, user, ids, vals, context=context)
