# -*- coding: utf-8 -*-
##############################################################################
#
#    Sidnei Brianti
#    
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from osv import osv

class launch_scpc(osv.osv):

    _inherit = 'res.partner'
    
    def open_scpc(self, cr, uid, ids, context=None):
        # Acrescentar o link do site de consulta abaixo
        url='http://'
        return {
        'type': 'ir.actions.act_url',
        'url':url,
        'target': 'new'
        }

    def open_rfb(self, cr, uid, ids, context=None):
        address_obj= self.pool.get('res.partner')
        partner = address_obj.browse(cr, uid, ids, context=context)[0]
        url_cnpj='http://www.receita.fazenda.gov.br/pessoajuridica/cnpj/cnpjreva/cnpjreva_solicitacao.asp'
        url_cpf='http://www.receita.fazenda.gov.br/aplicacoes/atcta/cpf/consultapublica.asp'
        
        if partner.is_company:
            url = url_cnpj
        else:
            url = url_cpf
        return {
        'type': 'ir.actions.act_url',
        'url':url,
        'target': 'new'
        }
    def open_sintegra(self, cr, uid, ids, context=None):
        address_obj= self.pool.get('res.partner')
        partner = address_obj.browse(cr, uid, ids, context=context)[0]
        if partner.state_id:
            uf=partner.state_id.code
        else:
           uf='XX'
        
        if uf=='RO':
            url='http://www.sefin.ro.gov.br/sint_consul.asp'
        elif uf == 'AC':
            url='http://www.sefaznet.ac.gov.br/sefazonline/servlet/sintegraconsulta'
        elif uf == 'AM':
            url='http://www.sefaz.am.gov.br/sintegra/sintegra0.asp'
        elif uf == 'RR':
            url='https://www.sefaz.rr.gov.br/sintegra/servlet/hwsintco'
        elif uf =='PA':
            url='http://app.sefa.pa.gov.br/Sintegra/'
        elif uf =='AP':
            url='http://www.sintegra.ap.gov.br/Sintegra/'
        elif uf == 'TO':
            url='http://sintegra.sefaz.to.gov.br/'
        elif uf == 'MA':
            url='http://sistemas.sefaz.ma.gov.br/sintegra/jsp/consultaSintegra/consultaSintegraFiltro.jsf'
        elif uf == 'PI':
            url='http://webas.sefaz.pi.gov.br/SintegraConsultaPublica/'
        elif uf == 'CE':
            url='http://www.sefaz.ce.gov.br/Sintegra/Sintegra.Asp?estado=CE'
        elif uf == 'RN':
            url='http://www.set.rn.gov.br/uvt/consultacontribuinte.aspx'
        elif uf =='PB':
            url='http://sintegra.receita.pb.gov.br/sintegra/sintegra.asp?estado=pb'
        elif uf == 'PE':
            url='http://www.sintegra.sefaz.pe.gov.br/'
        elif uf == 'AL':
            url='http://www.sefaz.al.gov.br/asp/sintegra/sintegra.asp?estado=AL'
        elif uf == 'SE':
            url='https://security.sefaz.se.gov.br/SIC/sintegra/index.jsp'
        elif uf == 'BA':
            url='http://www.sefaz.ba.gov.br/Sintegra/sintegra.asp?estado=BA'
        elif uf == 'MG':
            url='http://consultasintegra.fazenda.mg.gov.br/sintegra/'
        elif uf == 'ES':
            url='http://www.sintegra.es.gov.br/'
        elif uf == 'RJ':
            url='http://www.fazenda.rj.gov.br/projetoCPS'
        elif uf == 'SP':
            url='http://pfeserv1.fazenda.sp.gov.br/sintegrapfe/consultaSintegraServlet'
        elif uf == 'PR':
            url='http://www.sintegra.fazenda.pr.gov.br/sintegra/'
        elif uf == 'SC':
            url='http://sistemas.sef.sc.gov.br/sintegra'
        elif uf == 'RS':
            url='http://www.sefaz.rs.gov.br/asp/SEF_root/inf/sintegra_entrada.asp'
        elif uf =='MS':
            url='http://www1.sefaz.ms.gov.br/Cadastro/sintegra/cadastromsCCI.asp'
        elif uf == 'MT':
            url='http://www.sefaz.mt.gov.br/sid/consulta/infocadastral/consultar/publica'
        elif uf == 'GO':
            url='http://www.sefaz.go.gov.br/sintegra/sintegra.asp'
        elif uf == 'DF':
            url='http://www.fazenda.df.gov.br/area.cfm?id_area=110'
        else:
            url='http://www.sintegra.gov.br/new_bv.html'
        
        return {
        'type': 'ir.actions.act_url',
        'url':url,
        'target': 'new'
        }




launch_scpc()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

