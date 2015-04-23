class BloggsController < ApplicationController

  before_filter :authenticate_user!, :except => [:index, :show]

  def index
    @articles = Blogg.all
  end

  def show
    @article = Blogg.find(params[:id])
  end

  def new
    @article = Blogg.new
    authorize! :new, @article
  end

  def edit
    puts 'EDITING'
    puts params
    @article = Blogg.find(params[:id])
    authorize! :edit, @article
  end

  def create
    @article = Blogg.new(article_params)
    authorize! :create, @article
    if @article.save
      redirect_to @article
    else
      render :new
    end
  end

  def update
    @article = Blogg.find(params[:id])
    authorize! :update, @article
    if @article.update(article_params)
      redirect_to @article
    else
      render :edit
    end
  end

  def destroy
    @tempBlog = Blogg.find(params[:id])
    authorize! :destroy, @tempBlog
    @tempBlog.destroy

    redirect_to bloggs_path
  end

  private
  def article_params
    params.require(:blogg).permit(:title, :text)
  end
end
