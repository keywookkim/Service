import traceback

from flask         import jsonify, request
from flask.views   import MethodView
from flask_request_validator import (
    GET,
    PATH,
    Param,
    JSON,
    validate_params
)

from connection import get_connection
from utils      import catch_exception
from cache      import cache

class MainProductsView(MethodView):
    def __init__(self, service):
        self.service = service

    @cache.cached(timeout=30)
    def get(self):
        """
        메인페이지 상품리스트 - Presentation Layer(View) function
        Args:
            service: 서비스 레이어 객체
        Returns:
            200:    
                할인률이 존재하는 상품 & 판매량 상위 상품들로 묶은 리스트 JSONDATA
            400:
                {message : 모든 레이어에서 레이즈된 에러메시지}
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-09-22(김기욱) : 초기 생성
        """
        try :
            db = get_connection()
            products = self.service.get_main_products(db)

        except Exception as e:
            return jsonify({'message':f'{e}'}), 400
        
        else :
            return jsonify({'data' : products}), 200
        
        finally :
            db.close()


class CategorySetView(MethodView):
    def __init__(self, service):
        self.service = service

    @catch_exception
    @validate_params(
        Param('q', GET, int, required = True)
    )
    def get(self, q):
        """
        NAV/SIDE_BAR 카테고리리스트 - Presentation Layer(View) function
        Args:
            service: 서비스 레이어 객체
            q      : 쿼리파라미터(셀러속성아이디)
        Returns:
            200:    
                쿼리파라미터에 해당되는 카테고리 JSONDATA
            400:
                {message : 모든 레이어에서 레이즈된 에러메시지}
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-09-25(김기욱) : 초기 생성
        """
        try :
            db           = get_connection()
            category_set = self.service.get_category_set(q, db)
        
        except Exception as e:
            return jsonify({'message':f'{e}'}), 400
        
        else :
            return jsonify(category_set), 200
        
        finally :
            db.close()

class ProductsView(MethodView):
    def __init__(self, service):
        self.service = service

    @catch_exception
    @validate_params(
    #Validation_params 데코레이터를 통해 유효성 검사 후 통과한 파라미터들만 튜플로 반환
        Param('limit',  GET, int, default = 100, required = False),
        Param('offset', GET, int, required = False),
        Param('sp_id',  GET, int, required = False),
        Param('fc_id',  GET, int, required = False),
        Param('sc_id',  GET, int, required = False),
        Param('is_discounted', GET, bool, required = False),
        Param('is_popular', GET, bool, required = False),
        Param('is_new',   GET, bool, required = False),
        Param('is_cheap', GET, bool, required = False)
    )
    def get(self, *args):
        """
        전체상품 리스트(필터링있음) - Presentation Layer(View) function
        Args:
            service: 서비스 레이어 객체
            args = {
                'limit'         : 데이터의 최대 갯수,
                'offset'        : 페이지네이션 시작점,
                'sp_id'         : 셀러속성 별 필터링,
                'fc_id'         : 메인카테고리 별 필터링,
                'sc_id'         : 서브카테고리 별 필터링,
                'is_discounted' : 세일상품 필터링,
                'is_popular'    : 인기순 정렬,
                'is_new'        : 신상품 순 정렬,
                'is_cheap'      : 낮은 가격순 정렬
            }

        Returns:
            200:    
                쿼리파라미터에 해당되는 카테고리 JSONDATA
            400:
                {message : 모든 레이어에서 레이즈된 에러메시지}
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-09-28(김기욱) : 초기 생성
        """
        try :
            db = get_connection()
            #통과한 파라미터들을 딕셔너리 패킹
            params = {
                'limit'         :args[0],
                'offset'        :args[1],
                'sp_id'         :args[2],
                'fc_id'         :args[3],
                'sc_id'         :args[4],
                'is_discounted' :args[5],
                'is_popular'    :args[6],
                'is_new'        :args[7],
                'is_cheap'      :args[8]
            }
            products = self.service.get_products(params, db)
        
        except Exception as e:
            return jsonify({'message':f'{e}'}), 400
        
        else :
            return jsonify(products), 200
        
        finally :
            db.close() 

class ProductView(MethodView):
    def __init__(self, service):
        self.service = service
    
    @catch_exception
    @validate_params(
        Param('product_id', PATH, int, required = True)
    )
    @cache.cached(timeout=30)
    def get(self, product_id):
        """
        상품 상세페이지 - Presentation Layer(View) function
        Args:
            service    : 서비스 레이어 객체
            product_id : 상품아이디
        Returns:
            200:    
                상품상세 JSONDATA
            400:
                {message : 모든 레이어에서 레이즈된 에러메시지}
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-09-29(김기욱) : 초기 생성
        """
        try :
            db = get_connection()
            product = self.service.get_product(product_id, db)
        
        except Exception as e:
            return jsonify({'message':f'{e}'}), 400
        
        else:
            return jsonify(product), 200
        
        finally:
            db.close() 