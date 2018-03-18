from collections import namedtuple

import jinja2

HookType = namedtuple('HookType', 'name output inputs')
HookInput = namedtuple('HookInput', 'type name')
Hook = namedtuple('Hook', 'type name source_link')
HookSection = namedtuple('HookSection', 'name slug hooks')


def link(path):
    return 'https://github.com/postgres/postgres/blob/master/' + path


set_rel_pathlist_hook_type = HookType(
    name='set_rel_pathlist_hook_type',
    output='void',
    inputs=[
        HookInput('PlannerInfo *', 'root'),
        HookInput('RelOptInfo *', 'rel'),
        HookInput('Index', 'rti'),
        HookInput('RangeTblEntry *', 'rte'),
    ]
)
set_join_pathlist_hook_type = HookType(
    name='set_join_pathlist_hook_type',
    output='void',
    inputs=[
        HookInput('PlannerInfo *', 'root'),
        HookInput('RelOptInfo *', 'joinrel'),
        HookInput('RelOptInfo *', 'outerrel'),
        HookInput('RelOptInfo *', 'innerrel'),
        HookInput('JoinType', 'jointype'),
        HookInput('JoinPathExtraData *', 'extra'),
    ]
)
needs_fmgr_hook_type = HookType(
    name='needs_fmgr_hook_type',
    output='bool',
    inputs=[
        HookInput('Oid', 'fn_oid'),
    ]
)
fmgr_hook_type = HookType(
    name='fmgr_hook_type',
    output='void',
    inputs=[
        HookInput('FmgrHookEventType', 'event'),
        HookInput('FmgrInfo *', 'flinfo'),
        HookInput('Datum *', 'arg'),
    ]
)
object_access_hook_type = HookType(
    name='object_access_hook_type',
    output='void',
    inputs=[
        HookInput('ObjectAccessType', 'access'),
        HookInput('Oid', 'classId'),
        HookInput('Oid', 'objectId'),
        HookInput('int', 'subId'),
        HookInput('void *', 'arg'),
    ]
)
ExplainOneQuery_hook_type = HookType(
    name='ExplainOneQuery_hook_type',
    output='void',
    inputs=[
        HookInput('Query *', 'query'),
        HookInput('int', 'cursorOptions'),
        HookInput('IntoClause *', 'into'),
        HookInput('ExplainState *', 'es'),
        HookInput('const char *', 'queryString'),
        HookInput('ParamListInfo', 'params'),
        HookInput('QueryEnvironment *', 'queryEnv'),
    ]
)
explain_get_index_name_hook_type = HookType(
    name='explain_get_index_name_hook_type',
    output='const char *',
    inputs=[
        HookInput('Oid', 'indexId'),
    ]
)
check_password_hook_type = HookType(
    name='check_password_hook_type',
    output='void',
    inputs=[
        HookInput('const char *', 'username'),
        HookInput('const char *', 'shadow_pass'),
        HookInput('PasswordType', 'password_type'),
        HookInput('Datum', 'validuntil_time'),
        HookInput('bool', 'validuntil_null'),
    ]
)
ExecutorStart_hook_type = HookType(
    name='ExecutorStart_hook_type',
    output='void',
    inputs=[
        HookInput('QueryDesc *', 'queryDesc'),
        HookInput('int', 'eflags'),
    ]
)
ExecutorRun_hook_type = HookType(
    name='ExecutorRun_hook_type',
    output='void',
    inputs=[
        HookInput('QueryDesc *', 'queryDesc'),
        HookInput('ScanDirection', 'direction'),
        HookInput('uint64', 'count'),
        HookInput('bool', 'execute_once'),
    ]
)
ExecutorFinish_hook_type = HookType(
    name='ExecutorFinish_hook_type',
    output='void',
    inputs=[
        HookInput('QueryDesc *', 'queryDesc'),
    ]
)
ExecutorEnd_hook_type = HookType(
    name='ExecutorEnd_hook_type',
    output='void',
    inputs=[
        HookInput('QueryDesc *', 'queryDesc'),
    ]
)
ExecutorCheckPerms_hook_type = HookType(
    name='ExecutorCheckPerms_hook_type',
    output='bool',
    inputs=[
        HookInput('List', '*'),
        HookInput('', 'bool'),
    ]
)
ClientAuthentication_hook_type = HookType(
    name='ClientAuthentication_hook_type',
    output='void',
    inputs=[
        HookInput('Port', '*'),
        HookInput('', 'int'),
    ]
)
join_search_hook_type = HookType(
    name='join_search_hook_type',
    output='RelOptInfo *',
    inputs=[
        HookInput('PlannerInfo *', 'root'),
        HookInput('int', 'levels_needed'),
        HookInput('List *', 'initial_rels'),
    ]
)
get_relation_info_hook_type = HookType(
    name='get_relation_info_hook_type',
    output='void',
    inputs=[
        HookInput('PlannerInfo *', 'root'),
        HookInput('Oid', 'relationObjectId'),
        HookInput('bool', 'inhparent'),
        HookInput('RelOptInfo *', 'rel'),
    ]
)
planner_hook_type = HookType(
    name='planner_hook_type',
    output='PlannedStmt *',
    inputs=[
        HookInput('Query *', 'parse'),
        HookInput('int', 'cursorOptions'),
        HookInput('ParamListInfo', 'boundParams'),
    ]
)
create_upper_paths_hook_type = HookType(
    name='create_upper_paths_hook_type',
    output='void',
    inputs=[
        HookInput('PlannerInfo *', 'root'),
        HookInput('UpperRelationKind', 'stage'),
        HookInput('RelOptInfo *', 'input_rel'),
        HookInput('RelOptInfo *', 'output_rel'),
    ]
)
post_parse_analyze_hook_type = HookType(
    name='post_parse_analyze_hook_type',
    output='void',
    inputs=[
        HookInput('ParseState *', 'pstate'),
        HookInput('Query *', 'query'),
    ]
)
row_security_policy_hook_type = HookType(
    name='row_security_policy_hook_type',
    output='List *',
    inputs=[
        HookInput('CmdType', 'cmdtype'),
        HookInput('Relation', 'relation'),
    ]
)
shmem_startup_hook_type = HookType(
    name='shmem_startup_hook_type',
    output='void',
    inputs=[
    ]
)
ProcessUtility_hook_type = HookType(
    name='ProcessUtility_hook_type',
    output='void',
    inputs=[
        HookInput('PlannedStmt *', 'pstmt'),
        HookInput('const char *', 'queryString'),
        HookInput('ProcessUtilityContext', 'context'),
        HookInput('ParamListInfo', 'params'),
        HookInput('QueryEnvironment *', 'queryEnv'),
        HookInput('DestReceiver *', 'dest'),
        HookInput('char *', 'completionTag'),
    ]
)
emit_log_hook_type = HookType(
    name='emit_log_hook_type',
    output='void',
    inputs=[
        HookInput('ErrorData *', 'edata'),
    ]
)
get_attavgwidth_hook_type = HookType(
    name='get_attavgwidth_hook_type',
    output='int32',
    inputs=[
        HookInput('Oid', 'relid'),
        HookInput('AttrNumber', 'attnum'),
    ]
)
get_relation_stats_hook_type = HookType(
    name='get_relation_stats_hook_type',
    output='bool',
    inputs=[
        HookInput('PlannerInfo *', 'root'),
        HookInput('RangeTblEntry *', 'rte'),
        HookInput('AttrNumber', 'attnum'),
        HookInput('VariableStatData *', 'vardata'),
    ]
)
get_index_stats_hook_type = HookType(
    name='get_index_stats_hook_type',
    output='bool',
    inputs=[
        HookInput('PlannerInfo *', 'root'),
        HookInput('Oid', 'indexOid'),
        HookInput('AttrNumber', 'indexattnum'),
        HookInput('VariableStatData *', 'vardata'),
    ]
)

sections = [
    HookSection(
        'General hooks',
        'general-hooks',
        [
            Hook(
                needs_fmgr_hook_type,
                'needs_fmgr_hook',
                link('src/include/fmgr.h')
            ),
            Hook(
                fmgr_hook_type,
                'fmgr_hook',
                link('src/include/fmgr.h')
            ),
            Hook(
                object_access_hook_type,
                'object_access_hook',
                link('src/include/catalog/objectaccess.h')
            ),
            Hook(
                ExplainOneQuery_hook_type,
                'ExplainOneQuery_hook',
                link('src/include/commands/explain.h')
            ),
            Hook(
                explain_get_index_name_hook_type,
                'explain_get_index_name_hook',
                link('src/include/commands/explain.h')
            ),
            Hook(
                check_password_hook_type,
                'check_password_hook',
                link('src/include/commands/user.h')
            ),
            Hook(
                ExecutorStart_hook_type,
                'ExecutorStart_hook',
                link('src/include/executor/executor.h')
            ),
            Hook(
                ExecutorRun_hook_type,
                'ExecutorRun_hook',
                link('src/include/executor/executor.h')
            ),
            Hook(
                ExecutorFinish_hook_type,
                'ExecutorFinish_hook',
                link('src/include/executor/executor.h')
            ),
            Hook(
                ExecutorEnd_hook_type,
                'ExecutorEnd_hook',
                link('src/include/executor/executor.h')
            ),
            Hook(
                ExecutorCheckPerms_hook_type,
                'ExecutorCheckPerms_hook',
                link('src/include/executor/executor.h')
            ),
            Hook(
                ClientAuthentication_hook_type,
                'ClientAuthentication_hook',
                link('src/include/libpq/auth.h')
            ),
            Hook(
                set_rel_pathlist_hook_type,
                'set_rel_pathlist_hook',
                link('src/include/optimizer/paths.h')
            ),
            Hook(
                set_join_pathlist_hook_type,
                'set_join_pathlist_hook',
                link('src/include/optimizer/paths.h')
            ),
            Hook(
                join_search_hook_type,
                'join_search_hook',
                link('src/include/optimizer/paths.h')
            ),
            Hook(
                get_relation_info_hook_type,
                'get_relation_info_hook',
                link('src/include/optimizer/plancat.h')
            ),
            Hook(
                planner_hook_type,
                'planner_hook',
                link('src/include/optimizer/planner.h')
            ),
            Hook(
                create_upper_paths_hook_type,
                'create_upper_paths_hook',
                link('src/include/optimizer/planner.h')
            ),
            Hook(
                post_parse_analyze_hook_type,
                'post_parse_analyze_hook',
                link('src/include/parser/analyze.h')
            ),
            Hook(
                row_security_policy_hook_type,
                'row_security_policy_hook_permissive',
                link('src/include/rewrite/rowsecurity.h')
            ),
            Hook(
                row_security_policy_hook_type,
                'row_security_policy_hook_restrictive',
                link('src/include/rewrite/rowsecurity.h')
            ),
            Hook(
                shmem_startup_hook_type,
                'shmem_startup_hook',
                link('src/include/storage/ipc.h')
            ),
            Hook(
                ProcessUtility_hook_type,
                'ProcessUtility_hook',
                link('src/include/tcop/utility.h')
            ),
            Hook(
                emit_log_hook_type,
                'emit_log_hook',
                link('src/include/utils/elog.h')
            ),
            Hook(
                get_attavgwidth_hook_type,
                'get_attavgwidth_hook',
                link('src/include/utils/lsyscache.h')
            ),
            Hook(
                get_relation_stats_hook_type,
                'get_relation_stats_hook',
                link('src/include/utils/selfuncs.h')
            ),
            Hook(
                get_index_stats_hook_type,
                'get_index_stats_hook',
                link('src/include/utils/selfuncs.h')
            )
        ]
    )
]

if __name__ == '__main__':
    with open('Readme.md.in') as template_text:
        template = jinja2.Template(template_text.read())
        with open('Readme.generated.md', 'w') as f:
            f.write(template.render(sections=sections))

    with open('Detailed.md.in') as template_text:
        template = jinja2.Template(template_text.read())
        with open('Detailed.generated.md', 'w') as f:
            f.write(template.render(sections=sections))