/*
 * pipeline input parameters
 */
params.reads = "TEST"
log.info """\
         C O V I D - W O R K F L O W   M A N A G E R
         ===================================
         reads        : ${params.reads}
         """
         .stripIndent()
